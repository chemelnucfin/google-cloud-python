# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import google.cloud.firestore_v1beta1.proto.document_pb2 as google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2
import google.cloud.firestore_v1beta1.proto.firestore_pb2 as google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2


class FirestoreStub(object):
  """Specification of the Firestore API.

  The Cloud Firestore service.

  This service exposes several types of comparable timestamps:

  *    `create_time` - The time at which a document was created. Changes only
  when a document is deleted, then re-created. Increases in a strict
  monotonic fashion.
  *    `update_time` - The time at which a document was last updated. Changes
  every time a document is modified. Does not change when a write results
  in no modifications. Increases in a strict monotonic fashion.
  *    `read_time` - The time at which a particular state was observed. Used
  to denote a consistent snapshot of the database or the time at which a
  Document was observed to not exist.
  *    `commit_time` - The time at which the writes in a transaction were
  committed. Any read with an equal or greater `read_time` is guaranteed
  to see the effects of the transaction.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetDocument = channel.unary_unary(
        '/google.firestore.v1beta1.Firestore/GetDocument',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.GetDocumentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2.Document.FromString,
        )
    self.ListDocuments = channel.unary_unary(
        '/google.firestore.v1beta1.Firestore/ListDocuments',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListDocumentsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListDocumentsResponse.FromString,
        )
    self.CreateDocument = channel.unary_unary(
        '/google.firestore.v1beta1.Firestore/CreateDocument',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.CreateDocumentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2.Document.FromString,
        )
    self.UpdateDocument = channel.unary_unary(
        '/google.firestore.v1beta1.Firestore/UpdateDocument',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.UpdateDocumentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2.Document.FromString,
        )
    self.DeleteDocument = channel.unary_unary(
        '/google.firestore.v1beta1.Firestore/DeleteDocument',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.DeleteDocumentRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.BatchGetDocuments = channel.unary_stream(
        '/google.firestore.v1beta1.Firestore/BatchGetDocuments',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.BatchGetDocumentsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.BatchGetDocumentsResponse.FromString,
        )
    self.BeginTransaction = channel.unary_unary(
        '/google.firestore.v1beta1.Firestore/BeginTransaction',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.BeginTransactionRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.BeginTransactionResponse.FromString,
        )
    self.Commit = channel.unary_unary(
        '/google.firestore.v1beta1.Firestore/Commit',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.CommitRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.CommitResponse.FromString,
        )
    self.Rollback = channel.unary_unary(
        '/google.firestore.v1beta1.Firestore/Rollback',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.RollbackRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.RunQuery = channel.unary_stream(
        '/google.firestore.v1beta1.Firestore/RunQuery',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.RunQueryRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.RunQueryResponse.FromString,
        )
    self.Write = channel.stream_stream(
        '/google.firestore.v1beta1.Firestore/Write',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.WriteRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.WriteResponse.FromString,
        )
    self.Listen = channel.stream_stream(
        '/google.firestore.v1beta1.Firestore/Listen',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListenRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListenResponse.FromString,
        )
    self.ListCollectionIds = channel.unary_unary(
        '/google.firestore.v1beta1.Firestore/ListCollectionIds',
        request_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListCollectionIdsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListCollectionIdsResponse.FromString,
        )


class FirestoreServicer(object):
  """Specification of the Firestore API.

  The Cloud Firestore service.

  This service exposes several types of comparable timestamps:

  *    `create_time` - The time at which a document was created. Changes only
  when a document is deleted, then re-created. Increases in a strict
  monotonic fashion.
  *    `update_time` - The time at which a document was last updated. Changes
  every time a document is modified. Does not change when a write results
  in no modifications. Increases in a strict monotonic fashion.
  *    `read_time` - The time at which a particular state was observed. Used
  to denote a consistent snapshot of the database or the time at which a
  Document was observed to not exist.
  *    `commit_time` - The time at which the writes in a transaction were
  committed. Any read with an equal or greater `read_time` is guaranteed
  to see the effects of the transaction.
  """

  def GetDocument(self, request, context):
    """Gets a single document.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListDocuments(self, request, context):
    """Lists documents.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateDocument(self, request, context):
    """Creates a new document.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateDocument(self, request, context):
    """Updates or inserts a document.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteDocument(self, request, context):
    """Deletes a document.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchGetDocuments(self, request, context):
    """Gets multiple documents.

    Documents returned by this method are not guaranteed to be returned in the
    same order that they were requested.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BeginTransaction(self, request, context):
    """Starts a new transaction.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Commit(self, request, context):
    """Commits a transaction, while optionally updating documents.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Rollback(self, request, context):
    """Rolls back a transaction.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunQuery(self, request, context):
    """Runs a query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Write(self, request_iterator, context):
    """Streams batches of document updates and deletes, in order.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Listen(self, request_iterator, context):
    """Listens to changes.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListCollectionIds(self, request, context):
    """Lists all the collection IDs underneath a document.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FirestoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetDocument': grpc.unary_unary_rpc_method_handler(
          servicer.GetDocument,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.GetDocumentRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2.Document.SerializeToString,
      ),
      'ListDocuments': grpc.unary_unary_rpc_method_handler(
          servicer.ListDocuments,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListDocumentsRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListDocumentsResponse.SerializeToString,
      ),
      'CreateDocument': grpc.unary_unary_rpc_method_handler(
          servicer.CreateDocument,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.CreateDocumentRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2.Document.SerializeToString,
      ),
      'UpdateDocument': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateDocument,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.UpdateDocumentRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2.Document.SerializeToString,
      ),
      'DeleteDocument': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteDocument,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.DeleteDocumentRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'BatchGetDocuments': grpc.unary_stream_rpc_method_handler(
          servicer.BatchGetDocuments,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.BatchGetDocumentsRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.BatchGetDocumentsResponse.SerializeToString,
      ),
      'BeginTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.BeginTransaction,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.BeginTransactionRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.BeginTransactionResponse.SerializeToString,
      ),
      'Commit': grpc.unary_unary_rpc_method_handler(
          servicer.Commit,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.CommitRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.CommitResponse.SerializeToString,
      ),
      'Rollback': grpc.unary_unary_rpc_method_handler(
          servicer.Rollback,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.RollbackRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'RunQuery': grpc.unary_stream_rpc_method_handler(
          servicer.RunQuery,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.RunQueryRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.RunQueryResponse.SerializeToString,
      ),
      'Write': grpc.stream_stream_rpc_method_handler(
          servicer.Write,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.WriteRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.WriteResponse.SerializeToString,
      ),
      'Listen': grpc.stream_stream_rpc_method_handler(
          servicer.Listen,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListenRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListenResponse.SerializeToString,
      ),
      'ListCollectionIds': grpc.unary_unary_rpc_method_handler(
          servicer.ListCollectionIds,
          request_deserializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListCollectionIdsRequest.FromString,
          response_serializer=google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_firestore__pb2.ListCollectionIdsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.firestore.v1beta1.Firestore', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
