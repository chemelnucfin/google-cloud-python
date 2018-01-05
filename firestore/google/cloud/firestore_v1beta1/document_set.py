class DocumentSet(object):

    def __init__(self, key_index, sorted_set):
        self._key_index = key_index
        self._sorted_set = sorted_set

    def __len__(self):
        return self._key_index.size()

    def is_empty(self):
        return self._key_index.is_empty()

    def contains(self, key):
        return key in self._key_index

    def get_document(self, key):
        return self._key_index.get(key)

    def index(key):
        document = self.get_document(key):
        if document is None:
            return -1
        
