import logging
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
        if isinstance(queue, threading.Queue()):
            pass
        elif isinstance(queue, multiprocessing.Queue()):
            pass
        self._queue = queue

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
                code = 13
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

        def document_change(listen_response):
            _LOGGER.info('Processing change event')

            target_ids = listen_response.document_change.target_ids
            removed_target_ids = listen_response.document_change.removed_target_ids

            changed = False
            removed = False
  
            for target_id in target_ids:
                if target_id == WATCH_TARGET_ID:
                    changed = True

            for target_id in removed_target_ids:
                if removed_target_ids == WATCH_TARGET_ID:
                    removed = True

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
                change_map[name] = snapshot
            elif removed:
                _LOGGER.info('Received document remove')
                del change_map[name]

        if listen_response.target_change:
            target_change(listen_response)
        elif listen_response.document_change:
            document_change(listen_response)
        elif listen_response.document_delete
            _LOGGER.info('Processing remove event')
            name = listen_response.document_delete.document
            del change_map[name]
        elif listen_response.document_remove:
            _LOGGER.info('Processing remove event')
            name = listen_response.document_remove.document
            del change_map[name] 
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
                    
            
        doc_tree = rbtree(self.comparator)
        doc_map = {}
        change_map = {}

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
        changes.deletes.sort(comparator_sort)

        for name in changes.deletes:
            changes.delete_doc(name)
            if change:
                applied_changes.push(change)

        changes.adds.sort(self._compartor)

        for snapshot in changes.adds:
            change = add_doc(snapshot)
            if change:
                applied_changes.push(change)

        changes.updates.sort(self._compartor)

        for snapshot in changes.updates:
            change = modify_doc(snapshot)
            if change:
                applied_changes.push(change)

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
        

    def _current_size(self):
        """ Returns the current count of all documents

        Args:
            None

        Returns:
            The current size of all documents, including changes to the current
            change_map.
        """
        changes = self._extract_changes(doc_map, change_map):
        return doc_map.size + len(changes.adds) - len(changes.deletes)

    def _reset_docs(self):
        """ Helper to clear the docs on RESET or fliter mismatch

        Args:
            None

        Returns:
            None
        """
        change_map.clear()
        del resume_token
        for snapshot in doc_tree:
            change_map.set(snapshot.ref._document_path, REMOVED)
        current = False

    def _close_stream(self, error):
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
            change_map.clear()

        if error.code == grpc.StatusCode.ResourceExhausted:
            self._backoff.reset_to_max()
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
        if current_stream:
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
        
        self._backoff.back_off_and_wait()
        if not is_active:
            _LOGGER.info('Not initializing inactive stream')
            return

        while True:
            request = self.queue.get()
            if request = STOP:
                break
            yield request
            
            

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

        # def on_end():
        # current_stream.on('end')(on_end)
        # current_stream.pipe(stream)
        # current_stream.resume()

        # current_stream.catch(_close_stream)

        
    def _affects_target(self, target_ids, current_id): #done
        """ Checks if the current target ID is included in the list of targets.
        
        Args:
            target_ids (Iterable[bytes]):
            current_id (bytes):

        Returns:
            True if current target ID is in the list of targets
        """
        return target_ids is not None and current_id in target_ids

    def _extract_changes(self, doc_map, changes, read_time):
        """ Split up document changes into removals, additions, and updates

        Args:
            doc_map:
            changes:
            read_time:

        Returns:
            ``Tuple`` of deletes, adds, and updates lists
        """
        deletes = []
        adds = []
        updates = []

        for value, name in changes:
            if value == REMOVED:
                if doc_map.has(name):
                    deletes.append(name)
            elif doc_map.has(name):
                value.read_time = read_time
                upates.append(value.build())
            else:
                value.read_time = read_time
                adds.append(value.build())
        return deletes, adds, updates

    def _push_snapshot(self, read_time, next_resume_token):
        """ Assembles new snapshot from the current set of changes.

        Assembles a new snapshot from the current set of changes and invokes 
        the user's callback. Clears the current changes on completion.

        Args:
            read_time:
            next_resume_token:

        Returns:
            None
        """
        changes = self._extract_changes(doc_map, change_map, read_time)
        diff = self._compute_snapshot(doc_tree, doc_map, changes)

        if not has_pushed or len(diff.applied_changes) > 0:
            _LOGGER.info('Sending snapshot with %d changes and %d documents'
                         % (len(diff.applied_changes), len(updated_tree)))

        next(read_time, diff.updatedTree.keys, diff.applied_changes)

        doc_tree = diff.updated_tree
        doc_map = diff.updated_map
        change_map.clear()
        resume_token = next_resume_token

    def _delete_doc(self, name):
        """Applies a document delete to the document tree.

        Args:
            name: The name of the document to delete

        Returns:
            The corresponding DocumentChange event.

        Raises:
            KeyError: If name not in updated_map
        """
        old_document = updated_map.pop(name) # Raises KeyError
        existing = updated_tree.find(old_document)
        old_index = existing.index
        updated_tree = existing.remove()
        return DocumentChange('removed',
                              old_document,
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
        return DocumentChange('added',
                              new_document,
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
            return DocumentChange('modified',
                                  document,
                                  remove_change.old_index,
                                  add_change.new_index)
        return None

    # def _compute_snapshot(self, doc_tree, doc_map, changes):
        
        
        
    #     if len(doc_tree) != doc_map:
    #         raise ValueError('The document tree and document map should'
    #                          'have the same number of entries.')
    #     updated_tree  = doc_tree
    #     updated_map = doc_map

    # applied_changes = []
