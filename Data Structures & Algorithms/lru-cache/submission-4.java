class LRUCache {
    private ArrayList<int[]> cache;
    private int capacity;

    public LRUCache(int capacity) {
        this.cache = new ArrayList<>(); // [key, val]
        this.capacity = capacity;
    }
    
    public int get(int key) {
        for (int i = 0; i < cache.size(); i++) {
            if (cache.get(i)[0] == key) {
                int[] tmp = cache.remove(i);
                cache.add(tmp);
                return tmp[1];
            }
        }
        return -1;
    }
    
    public void put(int key, int value) {
        for (int i = 0; i < cache.size(); i++) {
            if (cache.get(i)[0] == key) {
                cache.remove(i);
                cache.add(new int[] {key, value});
                return;
            }
        }

        if (cache.size() == capacity) {
            cache.remove(0);
        }

        cache.add(new int[] {key, value});
    }
}
