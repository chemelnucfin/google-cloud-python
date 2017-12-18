# Copyright 2016 Google LLC All rights reserved.
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


import unittest


import six


class TestKeyRange(unittest.TestCase):

    def _getTargetClass(self):
        from google.cloud.spanner_v1.keyset import KeyRange

        return KeyRange

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _check_unused_keys(self, krange, used_keys):
        key_types = ('start_closed',
                     'start_open',
                     'end_closed',
                     'end_open')
        for key_type in key_types:
            if key_type not in used_keys:
                self.assertFalse(krange.to_pb().HasField(key_type))

    def test_ctor_no_start_no_end(self):
        with self.assertRaises(ValueError):
            self._make_one()

    def test_ctor_w_start_open_and_start_closed(self):
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        with self.assertRaises(ValueError):
            self._make_one(start_open=KEY_1, start_closed=KEY_2)

    def test_ctor_w_end_open_and_end_closed(self):
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        with self.assertRaises(ValueError):
            self._make_one(end_open=KEY_1, end_closed=KEY_2)

    def test_ctor_w_only_start_open(self):
        KEY_1 = [u'key_1']
        krange = self._make_one(start_open=KEY_1)
        self.assertEqual(krange.start_open, KEY_1)
        self.assertEqual(krange.start_closed, None)
        self.assertEqual(krange.end_open, None)
        self.assertEqual(krange.end_closed, None)

    def test_ctor_w_only_start_closed(self):
        KEY_1 = [u'key_1']
        krange = self._make_one(start_closed=KEY_1)
        self.assertEqual(krange.start_open, None)
        self.assertEqual(krange.start_closed, KEY_1)
        self.assertEqual(krange.end_open, None)
        self.assertEqual(krange.end_closed, None)

    def test_ctor_w_only_end_open(self):
        KEY_1 = [u'key_1']
        krange = self._make_one(end_open=KEY_1)
        self.assertEqual(krange.start_open, None)
        self.assertEqual(krange.start_closed, None)
        self.assertEqual(krange.end_open, KEY_1)
        self.assertEqual(krange.end_closed, None)

    def test_ctor_w_only_end_closed(self):
        KEY_1 = [u'key_1']
        krange = self._make_one(end_closed=KEY_1)
        self.assertEqual(krange.start_open, None)
        self.assertEqual(krange.start_closed, None)
        self.assertEqual(krange.end_open, None)
        self.assertEqual(krange.end_closed, KEY_1)

    def test_ctor_w_start_open_and_end_closed(self):
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        krange = self._make_one(start_open=KEY_1, end_closed=KEY_2)
        self.assertEqual(krange.start_open, KEY_1)
        self.assertEqual(krange.start_closed, None)
        self.assertEqual(krange.end_open, None)
        self.assertEqual(krange.end_closed, KEY_2)

    def test_ctor_w_start_closed_and_end_open(self):
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        krange = self._make_one(start_closed=KEY_1, end_open=KEY_2)
        self.assertEqual(krange.start_open, None)
        self.assertEqual(krange.start_closed, KEY_1)
        self.assertEqual(krange.end_open, KEY_2)
        self.assertEqual(krange.end_closed, None)

    def test_to_pb_w_start_closed_and_end_open(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange

        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        krange = self._make_one(start_closed=KEY_1, end_open=KEY_2)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        self.assertEqual(len(krange_pb.start_closed), 1)
        self.assertEqual(krange_pb.start_closed.values[0].string_value,
                         KEY_1[0])
        self.assertEqual(len(krange_pb.end_open), 1)
        self.assertEqual(krange_pb.end_open.values[0].string_value, KEY_2[0])

    def test_to_pb_w_start_open_and_end_closed(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange

        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        krange = self._make_one(start_open=KEY_1, end_closed=KEY_2)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        self.assertEqual(len(krange_pb.start_open), 1)
        self.assertEqual(krange_pb.start_open.values[0].string_value, KEY_1[0])
        self.assertEqual(len(krange_pb.end_closed), 1)
        self.assertEqual(krange_pb.end_closed.values[0].string_value, KEY_2[0])

    def test_ctor_empty_list_start_closed_and_key_end_closed(self):
        KEY_1 = [u'key_1']
        key_types = {'start_closed': [], 'end_closed': KEY_1}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_ctor_empty_list_start_closed_and_key_end_open(self):
        KEY_1 = [u'key_1']
        key_types = {'start_closed': [], 'end_open': KEY_1}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_ctor_empty_list_end_closed_and_key_start_closed(self):
        KEY_1 = [u'key_1']
        key_types = {'start_closed': KEY_1, 'end_closed': []}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_ctor_empty_list_end_open_and_key_start_closed(self):
        KEY_1 = [u'key_1']
        key_types = {'start_closed': KEY_1, 'end_open': []}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_ctor_empty_list_start_open_and_key_end_closed(self):
        KEY_1 = [u'key_1']
        key_types = {'start_open': [], 'end_closed': KEY_1}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_ctor_empty_list_start_open_and_key_end_open(self):
        KEY_1 = [u'key_1']
        key_types = {'start_open': [], 'end_open': KEY_1}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_ctor_empty_list_end_closed_and_key_start_open(self):
        KEY_1 = [u'key_1']
        key_types = {'start_open': KEY_1, 'end_closed': []}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_ctor_empty_list_end_open_and_key_start_open(self):
        KEY_1 = [u'key_1']
        key_types = {'start_open': KEY_1, 'end_open': []}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_empty_list_start_closed_and_key_end_closed(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange

        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_closed': [], 'end_closed': KEY_1}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            if key_types[key_type] == KEY_1:
                self.assertEqual(len(getattr(krange_pb, key_type)), 1)
                key1 = getattr(krange_pb, key_type).values[0].string_value
                self.assertEqual(key1, KEY_1[0])
            else:
                self.assertEqual(len(getattr(krange_pb, key_type)), 0)
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_empty_list_start_closed_and_key_end_open(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange

        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_closed': [], 'end_open': KEY_1}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            if key_types[key_type] == KEY_1:
                self.assertEqual(len(getattr(krange_pb, key_type)), 1)
                key1 = getattr(krange_pb, key_type).values[0].string_value
                self.assertEqual(key1, KEY_1[0])
            else:
                self.assertEqual(len(getattr(krange_pb, key_type)), 0)
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_empty_list_end_closed_and_key_start_closed(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange

        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_closed': KEY_1, 'end_closed': []}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            if key_types[key_type] == KEY_1:
                self.assertEqual(len(getattr(krange_pb, key_type)), 1)
                key1 = getattr(krange_pb, key_type).values[0].string_value
                self.assertEqual(key1, KEY_1[0])
            else:
                self.assertEqual(len(getattr(krange_pb, key_type)), 0)
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_empty_list_end_open_and_key_start_closed(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange

        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_closed': KEY_1, 'end_open': []}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            if key_types[key_type] == KEY_1:
                self.assertEqual(len(getattr(krange_pb, key_type)), 1)
                key1 = getattr(krange_pb, key_type).values[0].string_value
                self.assertEqual(key1, KEY_1[0])
            else:
                self.assertEqual(len(getattr(krange_pb, key_type)), 0)
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_empty_list_start_open_and_key_end_closed(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange

        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_open': [], 'end_closed': KEY_1}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            if key_types[key_type] == KEY_1:
                self.assertEqual(len(getattr(krange_pb, key_type)), 1)
                key1 = getattr(krange_pb, key_type).values[0].string_value
                self.assertEqual(key1, KEY_1[0])
            else:
                self.assertEqual(len(getattr(krange_pb, key_type)), 0)
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_empty_list_start_open_and_key_end_open(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange

        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_open': [], 'end_open': KEY_1}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            if key_types[key_type] == KEY_1:
                self.assertEqual(len(getattr(krange_pb, key_type)), 1)
                key1 = getattr(krange_pb, key_type).values[0].string_value
                self.assertEqual(key1, KEY_1[0])
            else:
                self.assertEqual(len(getattr(krange_pb, key_type)), 0)
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_empty_list_end_closed_and_key_start_open(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange

        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_open': KEY_1, 'end_closed': []}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            if key_types[key_type] == KEY_1:
                self.assertEqual(len(getattr(krange_pb, key_type)), 1)
                key1 = getattr(krange_pb, key_type).values[0].string_value
                self.assertEqual(key1, KEY_1[0])
            else:
                self.assertEqual(len(getattr(krange_pb, key_type)), 0)
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_empty_list_end_open_and_key_start_open(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange

        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_open': KEY_1, 'end_open': []}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            if key_types[key_type] == KEY_1:
                self.assertEqual(len(getattr(krange_pb, key_type)), 1)
                key1 = getattr(krange_pb, key_type).values[0].string_value
                self.assertEqual(key1, KEY_1[0])
            else:
                self.assertEqual(len(getattr(krange_pb, key_type)), 0)
        self._check_unused_keys(krange, used_keys)

    def test_ctor_keys_start_closed_end_closed(self):
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_closed': KEY_1, 'end_closed': KEY_2}
        krange = self._make_one(**key_types)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_ctor_keys_start_closed_end_open(self):
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_closed': KEY_1, 'end_open': KEY_2}
        krange = self._make_one(**key_types)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_ctor_keys_start_open_end_closed(self):
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_open': KEY_1, 'end_closed': KEY_2}
        krange = self._make_one(**key_types)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_ctor_keys_start_open_end_open(self):
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_open': KEY_1, 'end_open': KEY_2}
        krange = self._make_one(**key_types)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            self.assertEqual(getattr(krange, key_type), key_types[key_type])
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_keys_start_closed_end_closed(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_closed': KEY_1, 'end_closed': KEY_2}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            pb_key_type = getattr(krange_pb, key_type)
            self.assertEqual(len(pb_key_type), 1)
            self.assertEqual(pb_key_type.values[0].string_value,
                             key_types[key_type][0])
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_keys_start_closed_end_open(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_closed': KEY_1, 'end_open': KEY_2}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            pb_key_type = getattr(krange_pb, key_type)
            self.assertEqual(len(pb_key_type), 1)
            self.assertEqual(pb_key_type.values[0].string_value,
                             key_types[key_type][0])
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_keys_start_open_end_closed(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_open': KEY_1, 'end_closed': KEY_2}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            pb_key_type = getattr(krange_pb, key_type)
            self.assertEqual(len(pb_key_type), 1)
            self.assertEqual(pb_key_type.values[0].string_value,
                             key_types[key_type][0])
        self._check_unused_keys(krange, used_keys)

    def test_to_pb_keys_start_open_end_open(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeyRange
        KEY_1 = [u'key_1']
        KEY_2 = [u'key_2']
        key_types = {'start_open': KEY_1, 'end_open': KEY_2}
        krange = self._make_one(**key_types)
        krange_pb = krange.to_pb()
        self.assertIsInstance(krange_pb, KeyRange)
        used_keys = []
        for key_type in six.iterkeys(key_types):
            used_keys.append(key_type)
            pb_key_type = getattr(krange_pb, key_type)
            self.assertEqual(len(pb_key_type), 1)
            self.assertEqual(pb_key_type.values[0].string_value,
                             key_types[key_type][0])
        self._check_unused_keys(krange, used_keys)


class TestKeySet(unittest.TestCase):

    def _getTargetClass(self):
        from google.cloud.spanner_v1.keyset import KeySet

        return KeySet

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_ctor_w_all(self):
        keyset = self._make_one(all_=True)

        self.assertTrue(keyset.all_)
        self.assertEqual(keyset.keys, [])
        self.assertEqual(keyset.ranges, [])

    def test_ctor_w_keys(self):
        KEYS = [[u'key1'], [u'key2']]

        keyset = self._make_one(keys=KEYS)

        self.assertFalse(keyset.all_)
        self.assertEqual(keyset.keys, KEYS)
        self.assertEqual(keyset.ranges, [])

    def test_ctor_w_ranges(self):
        from google.cloud.spanner_v1.keyset import KeyRange

        range_1 = KeyRange(start_closed=[u'key1'], end_open=[u'key3'])
        range_2 = KeyRange(start_open=[u'key5'], end_closed=[u'key6'])

        keyset = self._make_one(ranges=[range_1, range_2])

        self.assertFalse(keyset.all_)
        self.assertEqual(keyset.keys, [])
        self.assertEqual(keyset.ranges, [range_1, range_2])

    def test_ctor_w_all_and_keys(self):

        with self.assertRaises(ValueError):
            self._make_one(all_=True, keys=[['key1'], ['key2']])

    def test_ctor_w_all_and_ranges(self):
        from google.cloud.spanner_v1.keyset import KeyRange

        range_1 = KeyRange(start_closed=[u'key1'], end_open=[u'key3'])
        range_2 = KeyRange(start_open=[u'key5'], end_closed=[u'key6'])

        with self.assertRaises(ValueError):
            self._make_one(all_=True, ranges=[range_1, range_2])

    def test_to_pb_w_all(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeySet

        keyset = self._make_one(all_=True)

        result = keyset.to_pb()

        self.assertIsInstance(result, KeySet)
        self.assertTrue(result.all)
        self.assertEqual(len(result.keys), 0)
        self.assertEqual(len(result.ranges), 0)

    def test_to_pb_w_only_keys(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeySet

        KEYS = [[u'key1'], [u'key2']]
        keyset = self._make_one(keys=KEYS)

        result = keyset.to_pb()

        self.assertIsInstance(result, KeySet)
        self.assertFalse(result.all)
        self.assertEqual(len(result.keys), len(KEYS))

        for found, expected in zip(result.keys, KEYS):
            self.assertEqual(len(found), len(expected))
            self.assertEqual(found.values[0].string_value, expected[0])

        self.assertEqual(len(result.ranges), 0)

    def test_to_pb_w_only_ranges(self):
        from google.cloud.spanner_v1.proto.keys_pb2 import KeySet
        from google.cloud.spanner_v1.keyset import KeyRange

        KEY_1 = u'KEY_1'
        KEY_2 = u'KEY_2'
        KEY_3 = u'KEY_3'
        KEY_4 = u'KEY_4'
        RANGES = [
            KeyRange(start_open=KEY_1, end_closed=KEY_2),
            KeyRange(start_closed=KEY_3, end_open=KEY_4),
        ]
        keyset = self._make_one(ranges=RANGES)

        result = keyset.to_pb()

        self.assertIsInstance(result, KeySet)
        self.assertFalse(result.all)
        self.assertEqual(len(result.keys), 0)
        self.assertEqual(len(result.ranges), len(RANGES))

        for found, expected in zip(result.ranges, RANGES):
            self.assertEqual(found, expected.to_pb())
