# Copyright 2017 Google LLC All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import functools
import glob
import json
import os
import unittest

import mock
from google.cloud.firestore_v1beta1.proto import test_pb2
from google.protobuf import text_format


class TestCrossLanguage(unittest.TestCase):

    def test_cross_language(self):
        filenames = sorted(glob.glob('tests/unit/testdata/*.textproto'))
# <<<<<<< HEAD
#         failed = 0
# =======
        count = 0
# >>>>>>> temp
        descs = []
        for test_filename in filenames:
            bytes = open(test_filename, 'r').read()
            test_proto = test_pb2.Test()
            text_format.Merge(bytes, test_proto)
            desc = '%s (%s)' % (
                test_proto.description,
                os.path.splitext(os.path.basename(test_filename))[0])
            try:
                self.run_write_test(test_proto, desc)
# <<<<<<< HEAD
#             except Exception:
#                 failed += 1
#                 # print(desc, test_proto)  # for debugging
#                 # print(error.args[0])  # for debugging
#                 descs.append(desc)
#         # for desc in descs:  # for debugging
#             # print(desc)  # for debugging
#         # print(str(failed) + "/" + str(len(filenames)))  # for debugging
# =======
            except (AssertionError, Exception) as error:
                import pdb
#                pdb.set_trace()
                count += 1
                print(desc, test_proto)
                print(error.args[0])
                descs.append(desc)
        for desc in descs:
            print(desc)
        print(str(count) + "/" + str(len(filenames)))
        raise
# >>>>>>> temp

    def run_write_test(self, test_proto, desc):
        from google.cloud.firestore_v1beta1.proto import firestore_pb2
        from google.cloud.firestore_v1beta1.proto import write_pb2

        # Create a minimal fake GAPIC with a dummy result.
        firestore_api = mock.Mock(spec=['commit'])
        commit_response = firestore_pb2.CommitResponse(
            write_results=[write_pb2.WriteResult()],
        )
        firestore_api.commit.return_value = commit_response

        kind = test_proto.WhichOneof("test")
        call = None
        if kind == "create":
            tp = test_proto.create
            client, doc = self.setup(firestore_api, tp)
            data = convert_data(json.loads(tp.json_data))
            call = functools.partial(doc.create, data)
            # import pdb
            # pdb.set_trace()
        elif kind == "get":
            tp = test_proto.get
            client, doc = self.setup(firestore_api, tp)
# <<<<<<< HEAD
#             call = functools.partial(doc.get, None, None)
# =======
            try:
                field_paths = tp.field_paths
            except AttributeError:
                field_paths = None
            try:
                transaction = tp.transaction
            except AttributeError:
                transaction = None
            
            call = functools.partial(doc.get, field_paths, transaction)
# >>>>>>> temp
            try:
                tp.is_error
            except AttributeError:
                return
        elif kind == "set":
            tp = test_proto.set
            client, doc = self.setup(firestore_api, tp)
            data = convert_data(json.loads(tp.json_data))
            if (
                "set-10" in desc or
                "set-15" in desc or
                "set-16" in desc or
                "set-3" in desc or
                "set-7" in desc or
                "set-9" in desc
#                    "set-8" in desc or
#                "set-16" in desc or
#                "set-17" in desc or
#                "set-18" in desc or
#                "set-19" in desc or
#                "set-21" in desc or
#                "set-22" in desc or
#                "set-23" in desc or
#                "set-24" in desc or
#                "set-25" in desc or
#                "set-26" in desc
            ):
                import pdb
                pdb.set_trace()
                
            if tp.HasField("option"):
                option = convert_set_option(tp.option, data)
            else:
                option = None
            call = functools.partial(doc.set, data, option)
# >>>>>>> temp
        elif kind == "update":
            tp = test_proto.update
            client, doc = self.setup(firestore_api, tp)
            data = convert_data(json.loads(tp.json_data))
            if tp.HasField("precondition"):
                option = convert_precondition(tp.precondition)
            else:
                option = None
            call = functools.partial(doc.update, data, option)
        elif kind == "update_paths":
# <<<<<<< HEAD
#             # Python client doesn't have a way to call update with
#             # a list of field paths.
#             return
# =======
            return
            # tp = test_proto.update_paths
            # client, doc = self.setup(firestore_api, tp)
            # field_paths = tp.field_paths
            # paths = []
            # for field_path in field_paths:
            #     paths.append(field_path.field[0])
            # try:
            #     data = convert_data(json.loads(tp.json_values[0]))
            # except:
            #     data = None
            # try:
            #     request = tp.request
            # except:
            #     request = None
            # call = functools.partial(doc.update, (paths, data, request))
# >>>>>>> temp
        else:
            assert kind == "delete"
            tp = test_proto.delete
            client, doc = self.setup(firestore_api, tp)
            if tp.HasField("precondition"):
                option = convert_precondition(tp.precondition)
            else:
                option = None
            call = functools.partial(doc.delete, option)

        if tp.is_error:
            # TODO: is there a subclass of Exception we can check for?
            with self.assertRaises(Exception):
                call()
            
        else:
            call()
            firestore_api.commit.assert_called_once_with(
                client._database_string,
                list(tp.request.writes),
                transaction=None,
                metadata=client._rpc_metadata)

    def setup(self, firestore_api, proto):
        from google.cloud.firestore_v1beta1 import Client
        from google.cloud.firestore_v1beta1.client import DEFAULT_DATABASE
        import google.auth.credentials

        _, project, _, database, _, doc_path = proto.doc_ref_path.split('/', 5)
        self.assertEqual(database, DEFAULT_DATABASE)

        # Attach the fake GAPIC to a real client.
        credentials = mock.Mock(spec=google.auth.credentials.Credentials)
        client = Client(project=project, credentials=credentials)
        client._firestore_api_internal = firestore_api
        return client, client.document(doc_path)


def convert_data(v):
    # Replace the strings 'ServerTimestamp' and 'Delete' with the corresponding
    # sentinels.
    from google.cloud.firestore_v1beta1 import SERVER_TIMESTAMP, DELETE_FIELD

    if v == 'ServerTimestamp':
        return SERVER_TIMESTAMP
    elif v == 'Delete':
        return DELETE_FIELD
    elif isinstance(v, list):
        return [convert_data(e) for e in v]
    elif isinstance(v, dict):
        return {k: convert_data(v2) for k, v2 in v.items()}
    else:
        return v


def convert_set_option(option, data):
    from google.cloud.firestore_v1beta1.client import MergeOption
    from google.cloud.firestore_v1beta1 import _helpers
    if isinstance(option, test_pb2.SetOption):
        if option.all:
            # import pdb
            # pdb.set_trace()
            field_paths = _helpers.extract_field_paths(data)
            field_paths = [_helpers.FieldPath(*field_path) for field_path in field_paths]
            return field_paths
        else:
            fields = []
            for field in option.fields:
#                fields.append(_helpers.FieldPath(*field.field).to_api_repr())
                fields.append(_helpers.FieldPath(*field.field)) 
            return fields


def convert_precondition(precond):
    from google.cloud.firestore_v1beta1 import Client

    if precond.HasField('exists'):
        return Client.write_option(exists=precond.exists)
    else:  # update_time
        return Client.write_option(last_update_time=precond.update_time)
