import logging
import namedtuple
import threading
import multiprocessing

import grpc

from api_core import exceptions
from api_core import retry
from google.cloud.firestore_v1beta1 import _helpers
from google.cloud.firestore_v1beta1.collections import document_set

_LOGGER = logging.getLogger(__name__)
_INITIAL_SLEEP = 1.0
_MAXIMUM_DELAY = 60.0


class Watch(object):

    WATCH_TARGET_ID = 0xe0
    
    def __init__(self, firestore, target, comparator, queue=threading.queue()):
        """ Object for realtime listen of a firestore document

        Args:
            firestore: :class:`firestore.client.Client`: The
                Firestore Database client.
            target: A Firestore 'Target' proto denoting the target to
                listen on.
            comparator: A comparator for DocumentSnapshots that is used
                to order the document
        """
        self._firestore = firestore
        self._api = firestore._firestore_api_internal
        self._targets = target
        self._comparator = comparator
        self._backoff = retry.exponential_sleep_generator(_INITIAL_SLEEP,
                                                          _MAXIMUM_DELAY)
        self._queue = threading.queue

    @classmethod
    def for_document(cls, document_reference): #done
        """ Creates a new Watch instance that listens on DocumentReferences.

        Args:
            document_reference: The document reference used for this watch.

        Returns:
            :class:`firestore.watch.Watch`: A newly created Watch instance.
        """
        def document_comparator(this, that):
            if this != that:
                raise ValueError('Should only receive one document '
                                 'for DocumentReference listeners')
            return 0
        
        return cls(document_reference._client,
                   {documents:
                        {documents: [document_reference._document_path]},
                    target_id: WATCH_TARGET_ID,
                   },
                   document_comparator)


    @classmethod
    def for_query(cls, query): #done
        """ Creates a new Watch instance that listens on Queries.

        Args:
            query: The query used for this watch.

        Returns:
            :class:`firestore.watch.Watch`:A newly created Watch instance.
        """
        return cls(query.firestore,
                   {query: query._to_protobuf(),
                    target_id: WATCH_TARGET_ID
                   }
                   query.comparator())

    def on_next(self, listen_response):

        def target_change(listen_response)
            _LOGGER.log('Processing target change')
            change = listen_response.target_change
            no_target_ids = not target_ids
            if change.target_change_type == 'NO_CHANGE':
                if no_target_ids and change.read_time and self.current:
                    self._push_snapshot(change.read_time, change.resume_token)
            elif change.target_change_type == 'ADD':
                if WATCH_TARGET_ID != change.target_ids[0]:
                    raise ValueError('Unexpected target ID sent by server')
            elif change.target_change_type == 'REMOVE':
                code = grpc.StatusCode.CANCELLED
                message = 'internal error'
                if change.cause:
                    code = change.cause.code
                    message = change.cause.message
                self._close_stream(Error('Error ' + code + ': '  + message))
            elif change.target_change_type == 'RESET':
                self._reset_docs()
            elif change.target_change_type == 'CURRENT':
                current = true
            else:
                self._close_stream(Error('Unknown target change type: '
                                   + str(change)))
            if (change.resume_token is not None
                    and self._affects_target(change.get_target_ids_list(), 
                                             WATCH_TARGET_ID)
            ):
                self.next_attempt = next(self._backoff)
                                         

        def document_change(listen_response):
            _LOGGER.info('Processing change event')

            target_ids = listen_response.document_change.target_ids
            removed_target_ids = listen_response.document_change.removed_target_ids

            changed = target_ids and target_id in target_ids
            removed = target_ids and target_id in removed_target_ids
  
            document = listen_response.document_change.document
            name = document.name

            if changed:
                _LOGGER.info('Received document change')
                snapshot = DocumentSnapshot(DocumentReference(self._firestore, ResourcePath.from_slash_separated_string(name)),
                                            document.fields,
                                            True,
                                            Documentread_time,
                                            DocumentSnapshot.to_ISO_time(
                                                document.create_time),
                                            DocumentSnapshot.to_ISO_time(
                                                document.update_time)
                                            )
                self._change_map[name] = snapshot
            elif removed:
                _LOGGER.info('Received document remove')
                self._change_map.pop('name', None)

        if listen_response.target_change:
            target_change(listen_response)
        elif listen_response.document_change:
            document_change(listen_response)
        elif listen_response.document_delete
            _LOGGER.info('Processing remove event')
            name = listen_response.document_delete.document
            self._change_map.pop('name', None)
        elif listen_response.document_remove:
            _LOGGER.info('Processing remove event')
            name = listen_response.document_remove.document
            self._change_map.pop('name', None)
        elif listen_response.filter:
            _LOGGER.info('Processing filter update')
            if listen_response.filter.count != self._current_size():
                self._reset_docs()
                self._reset_stream()
        else:
            self._close_stream(Error('Unknown listen response type: ' + str(proto)))

    @synchronized
    def on_error(self, error):
        """ Called if the listen fails or is cancelled

        Args:
            error: The error that caused the failed

        Returns:
            None
        """
        self._maybe_reopen_stream(error)

    @synchronized
    def on_completed(self):
        """ Called if the stream ended unexpectedly
        
        Args:
            None

        Returns:
            None
        """
        error = Error('Stream ended unexpectedly')
        error.code = grpc.StatusCode.UNKNOWN
        self._maybe_reopen_stream(error)

    def run_watch(self, firestore_api):
        self._is_active = False
        self._current = False
        self._document_set = DocumentSet()
        self._change_map = {}
        self._resume_token = None
        self._has_pushed = False
#        self._lock = threading.Lock()
        
        requests = self._init_stream()
        try:
            responses = self._firestore_api_internal.listen(requests)
            for response in responses:
                self.on_next(response)
        except google.gax.errors.GaxError as exc_info:
            self.on_error(exc_info)
                    
            
        current = False
        has_pushed = False
        is_active = True

        REMOVED = {}

        request = {database: self._firestore._document_path,
                   add_target: self._targets
        }

        stream = through.obj()

        current_stream = None

        def comparator_sort(name1, name2):
            return self._comparator(updated_map[name1], updated_map[name2])
        if not len(updated_tree) == len(updated_map):
            raise RuntimeError('The update document tree and document '
                               'map should have the same number of '
                               'entries')

        return {updated_tree, updated_map, applied_changes)



        init_stream()

        stream.on('data', proto) # ??

        def on_end():
            _LOGGER.info('Processing stream end')
            if current_stream:
                current_stream.end()

        on('end', on_end)

        def initialize():
            return {}

        def end_stream():
            _LOGGER.info('Ending stream')
            is_active = False
            on_next = initialize
            on_error = initialize
            stream.end()

        return end_stream
        

    def _current_size(self): #done
        """ Returns the current count of all documents

        Args:
            None

        Returns:
            The current size of all documents, including changes to the current
            change_map.
        """
        changes = self._extract_changes(self.read_time)
        return self._document_set.size + len(changes.adds) - len(changes.deletes)

    def _reset_docs(self): #done
        """ Helper to clear the docs on RESET or fliter mismatch

        Args:
            None

        Returns:
            None
        """
        self._change_map.clear()
        del resume_token
        for snapshot in self._document_set:
            self._change_map[snapshot.reference.path] = None
        current = False

    def _close_stream(self, error): #done
        """ Closes the stream and calls onError() if the stream is still active.

        Args:
            error: The error that invoked this close

        Returns:
            None
        """
        if current_stream is not None:
            current_stream.on_completed()
            current_stream = None
        stream.end()

        if self._is_active:
            self._is_active = False
            _LOGGER.error('Invoking on_error: ', error)
            self.on_error(error)

    def _maybe_reopen_stream(self, error):
        """ Reopens stream if error is not permanent

        Re-opens the stream unless the specified error is considered permanent.
        Clears the change map.

        Args:
            error: The error that invoked this close

        Returns:
            None
        """
        if self._is_active and not exceptions.is_permanent_error(error):
            _LOGGER.error('Stream ended, re-opening after;'
                          'retryable error: ',
                          error)
            request.add_target.resume_token = resume_token
            self._change_map.clear()

        if error.code == grpc.StatusCode.ResourceExhausted:
            next(self._backoff)
            self._reset_stream()
        else:
            _LOGGER.error('Stream ended, sending error: ', error)
            self._close_stream(error)

    def _reset_stream(self):
        """ Helper to restart the outgoing stream to the backend

        Args:
            None

        Returns:
            None
        """
        _LOGGER.info('Opening new stream')
        if current_stream is not None:
            current_stream.unpipe(stream)
            current_stream.end()
            current_stream = None
            init_stream()

    def _init_stream(self):
        """ Initializes a new stream to the backend with backoff

        Args:
            None

        Returns:
            None
        """
        

        if not self.is_active:
            _LOGGER.info('Not initializing inactive stream')
            return

        while True:
            request = self.queue.get()
            if request = STOP:
                break
            yield request
            self._backoff.back_off_and_wait()            
            

        backend_stream = self._firestore.read_write_stream(
            self._api.Firestore._listen.bind(self._api.Firestore),
            request,
        )

        if not self.is_active:
            _LOGGER.info('Closing inactive stream')
            backend_stream.end()
        _LOGGER.info('Opened new stream')
        current_stream = backend_stream

        current_stream.on('error')(on_error)

    def _affects_target(self, target_ids, current_id): #done
        """ Checks if the current target ID is included in the list of targets.
        
        Args:
            target_ids (Iterable[bytes]):
            current_id (bytes):

        Returns:
            True if current target ID is in the list of targets
        """
        return target_ids is not None and current_id in target_ids

    def _extract_changes(self, changes, read_time): #done
        """ Split up document changes into removals, additions, and updates

        Args:
            self._document_set:
            changes:
            read_time:

        Returns:
            ``collections.namedtuple`` of deletes, adds, and updates lists
        """
        change_set = collections.namedtuple('ChangeSet',
                                            ['deletes', 'adds', 'updates'])
        change_set.deletes = []
        change_set.adds = []
        change_set.updates = []

        for value, name in changes:
            if value is None:
                if self._document_set.has(name):
                    change_set.deletes.append(name)
            elif self._document_set.has(name):
                value.read_time = read_time
                change_set.upates.append(value.build())
            else:
                value.read_time = read_time
                change_set.adds.append(value.build())
        return change_set

    def _push_snapshot(self, read_time, next_resume_token): 
        """ Assembles new snapshot from the current set of changes.

        Assembles a new snapshot from the current set of changes and invokes 
        the user's callback. Clears the current changes on completion.

        Args:
            read_time: Read time of the snapshot obtained
            next_resume_token: The server assigned resume token

        Returns:
            None
        """
        diff = self._compute_snapshot(read_time)

        if not has_pushed or len(diff) > 0:
            _LOGGER.info('Sending snapshot with %d changes and %d documents'
                         % (len(diff.applied_changes), len(updated_tree)))

        next(read_time, diff.updatedTree.keys, diff.applied_changes)

        doc_tree = diff.updated_tree
        self._document_set = diff.updated_map
        change_map.clear()
        resume_token = next_resume_token

    def _delete_doc(self, old_document): #done
        """Applies a document delete to the document tree.

        Args:
            old_document (DocumentSnapshot): The document snapshot to delete

        Returns:
            :class:~`DocumentChange`: The corresponding DocumentChange event.
        """
        resource_path = old_document.reference.path
        old_index = document_set.index(resource_path)
        document_set = docuemnt_set.remove(resource_path)
        return DocumentChange(old_document,
                              DocumentChange.REMOVED,
                              old_index,
                              -1)

    def _add_doc(self, new_document):
        """Applies a document add to the document tree.

        Args:
            new_document: The name of the document to add

        Returns:
            The corresponding DocumentChange event.

        Raises:
            ValueError: If new_document already exists
        """
        name = new_document._document_path
        if name in updated_map:
            raise ValueError('Document to add already exists')
        updated_tree = updated_tree.insert(new_document, null)
        new_index = updated_tree.find(new_document).index
        updated_map[name] = new_document
        return DocumentChange(new_document,
                              DocumentChange.ADDED,
                              -1,
                              new_index)

    def _modify_doc(self, document):
        """Applies a document modification to the document tree.

        Args:
            document: The name of the document to add

        Returns:
            The corresponding DocumentChange event for successful modifications.

        Raises:
            ValueError: If document does not exist
        """
        name = document.ref._document_path
        if not name in self._document_set.key_index:
            raise ValueError('Document to modify does not exist')
        old_document = self._document_set.index(name)
        if old_document == -1
        if old_document.update_time != document.update_time:
            remove_change = delete_doc(name)
            add_change = add_doc(document)
            return DocumentChange(document,
                                  DocumentChange.MODIFIED,
                                  remove_change.old_index,
                                  add_change.new_index)
        return None

    def _compute_snapshot(self, read_time): #done
        """ Applies the mutations in change_set to the document_set. 

        Applies the mutations in change_set to the document_set. Modifies
        document_set in place and returns the applied DocumentChange events.

        Args:
            read_time(:class:`~datetime.datetime`): 
                The time at which this snapshot was obtained.

        Returns:
            List(~.firestore_v1beta1.document_change.DocumentChange):
                The changed documents.
        """
        applied_changes = []
        change_set = self._extract_changes(read_time)

        change_set.deletes.sort(cmp=self._comparator)

        for delete in change_set.deletes:
            applied_changes.append(self._delete_doc(delete))

        change_set.adds.sort(self._compartor)

        for add in change_set.adds:
            applied_changes.append(self._add_doc(add))

        change_set.updates.sort(self._compartor)

        for update in change_set.updates:
            change = self._modify_doc(update)
            if change is not None:
                applied_changes.push(change)

