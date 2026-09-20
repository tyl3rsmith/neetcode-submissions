class Node {
    private int key;
    private int val;
    private Node prev;
    private Node next;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }

    public int getKey() {
        return this.key;
    }

    public int getValue() {
        return this.val;
    }

    public Node getPrev() {
        return this.prev;
    }

    public Node getNext() {
        return this.next;
    }

    public void setKey(int key) {
        this.key = key;
    }

    public void setValue(int val) {
        this.val = val;
    }

    public void setPrev(Node prev) {
        this.prev = prev;
    }

    public void setNext(Node next) {
        this.next = next;
    }
}

class LRUCache {
    private int capacity;
    private Map<Integer, Node> cache; // key -> node
    private Node lru;
    private Node mru;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();

        this.lru = new Node(0, 0); // points at lru
        this.mru = new Node(0, 0); // points at mru

        // initially lru and mru are connected
        this.lru.setNext(this.mru);
        this.mru.setPrev(this.lru);
    }

    public void remove(Node node) {
        // remove from the list
        Node prev = node.getPrev();
        Node next = node.getNext();
        prev.setNext(next);
        next.setPrev(prev);
        
    }

    public void insert(Node node) {
        // insert at the mru
        Node prev = mru.getPrev();
        prev.setNext(node);
        node.setPrev(prev);
        node.setNext(mru);
        mru.setPrev(node);
    }
    
    public int get(int key) {
        if (cache.containsKey(key)) {
            // update most recent
            remove(cache.get(key));
            insert(cache.get(key));
            return cache.get(key).getValue();
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            remove(cache.get(key));      
        }

        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        insert(newNode);

        if (cache.size() > capacity) {
            Node lruNode = lru.next;
            remove(lruNode);
            cache.remove(lruNode.key);
        }
    }
}
