class TimeMap {
    // HashMap: key -> List of pairs (timestamp, value)
    private Map<String, List<List<String>>> store;

    public TimeMap() {
        store = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (!store.containsKey(key)) {
            store.put(key, new ArrayList<>());
        }
        store.get(key).add(Arrays.asList(String.valueOf(timestamp), value));
    }
    
    public String get(String key, int timestamp) {
        if (!store.containsKey(key)) {
            return "";
        }

        int resIdx = -1;
        int l = 0, r = store.get(key).size() - 1;

        while (l <= r) {
            int m = l + (r - l) / 2;
            int time = Integer.parseInt(store.get(key).get(m).get(0));

            if (time <= timestamp) {
                resIdx = m;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return resIdx == -1 ? "" : store.get(key).get(resIdx).get(1);
    }
}
