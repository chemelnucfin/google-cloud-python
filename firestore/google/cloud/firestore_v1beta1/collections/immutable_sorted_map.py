class ImmutableSortedMap(object):
    def containsKey(self, key):
        raise NotImplemented

    def get(self, key):
        raise NotImplemented

    def remove(self, key):
        raise NotImplemented

    def insert(self, key, value):
        raise NotImplemented

    def getMinKey(self):
        raise NotImplemented

    def getMaxKey(self):
        raise NotImplemented

    def int size():
        raise NotImplemented

    def isEmpty():
        raise NotImplemented

    def void inOrderTraversal(LLRBNode.NodeVisitor<K, V> visitor):
        raise NotImplemented

    def Iterator<Map.Entry<K, V>> iterator():
        raise NotImplemented

    def Iterator<Map.Entry<K, V>> iteratorFrom(K key):
        raise NotImplemented

    def Iterator<Map.Entry<K, V>> reverseIteratorFrom(K key):
        raise NotImplemented

    def Iterator<Map.Entry<K, V>> reverseIterator():
        raise NotImplemented

    def K getPredecessorKey(K key):
        raise NotImplemented

    def K getSuccessorKey(K key):
        raise NotImplemented

    def int indexOf(K key):
        raise NotImplemented

    def Comparator<K> getComparator():
        raise NotImplemented

    def __eq__(self, other):
        if isinstance(other, ImmutableSortedMap):
            return False
        if self.get_comparator() != other.get_comparator():
            return False
        if self.size() != other.size():
            return False
        for this, that in zip(iter(self), iter(other)):
            if this != that):
                return False
        return True

    def __hash__(self):
        result = hash(self.get_comparator())
        for entry in self:
            result = 31 * result + hash(entry)
        return result

    def __str__(self):
        name = self.__class__.__name__
        b += '{'
        first = True
        for entry in self:
            if first:
                first = False
            else:
                b += ','
            b += '(%s=>%s)' % entry
        b += '};'

  @Override
  @SuppressWarnings("unchecked")
  public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof ImmutableSortedMap)) return false;

    ImmutableSortedMap<K, V> that = (ImmutableSortedMap) o;

    if (!this.getComparator().equals(that.getComparator())) return false;
    if (this.size() != that.size()) return false;

    Iterator<Map.Entry<K, V>> thisIterator = this.iterator();
    Iterator<Map.Entry<K, V>> thatIterator = that.iterator();
    while (thisIterator.hasNext()) {
      if (!thisIterator.next().equals(thatIterator.next())) return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    int result = this.getComparator().hashCode();
    for (Map.Entry<K, V> entry : this) {
      result = 31 * result + entry.hashCode();
    }

    return result;
  }

  public String toString() {
    StringBuilder b = new StringBuilder();
    b.append(this.getClass().getSimpleName());
    b.append("{");
    boolean first = true;
    for (Map.Entry<K, V> entry : this) {
      if (first) first = false;
      else b.append(", ");
      b.append("(");
      b.append(entry.getKey());
      b.append("=>");
      b.append(entry.getValue());
      b.append(")");
    }
    b.append("};");
    return b.toString();
  }

  public static class Builder {
    /**
     * The size threshold where we use a tree backed sorted map instead of an array backed sorted
     * map. This is a more or less arbitrary chosen value, that was chosen to be large enough to fit
     * most of object kind of Database data, but small enough to not notice degradation in
     * performance for inserting and lookups. Feel free to empirically determine this constant, but
     * don't expect much gain in real world performance.
     */
    static final int ARRAY_TO_RB_TREE_SIZE_THRESHOLD = 25;

    public static <K, V> ImmutableSortedMap<K, V> emptyMap(Comparator<K> comparator) {
      return new ArraySortedMap<K, V>(comparator);
    }

    public interface KeyTranslator<C, D> {
      public D translate(C key);
    }

    private static final KeyTranslator IDENTITY_TRANSLATOR =
        new KeyTranslator() {
          @Override
          public Object translate(Object key) {
            return key;
          }
        };

    @SuppressWarnings("unchecked")
    public static <A> KeyTranslator<A, A> identityTranslator() {
      return IDENTITY_TRANSLATOR;
    }

    public static <A, B> ImmutableSortedMap<A, B> fromMap(
        Map<A, B> values, Comparator<A> comparator) {
      if (values.size() < ARRAY_TO_RB_TREE_SIZE_THRESHOLD) {
        return ArraySortedMap.fromMap(values, comparator);
      } else {
        return RBTreeSortedMap.fromMap(values, comparator);
      }
    }

    public static <A, B, C> ImmutableSortedMap<A, C> buildFrom(
        List<A> keys,
        Map<B, C> values,
        ImmutableSortedMap.Builder.KeyTranslator<A, B> translator,
        Comparator<A> comparator) {
      if (keys.size() < ARRAY_TO_RB_TREE_SIZE_THRESHOLD) {
        return ArraySortedMap.buildFrom(keys, values, translator, comparator);
      } else {
        return RBTreeSortedMap.buildFrom(keys, values, translator, comparator);
      }
    }
  }
}

    
