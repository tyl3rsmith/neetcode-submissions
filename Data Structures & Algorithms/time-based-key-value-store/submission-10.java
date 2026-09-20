class TimeMap {
    // HashMap -> key -> HashMap -> timestamp, list of values
    private Map<String, Map<Integer, List<String>>> store;

    public TimeMap() {
        store = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (!store.containsKey(key)) {
            store.put(key, new HashMap<>());
        }
        if (!store.get(key).containsKey(timestamp)) {
            store.get(key).put(timestamp, new ArrayList<>());
        }
        store.get(key).get(timestamp).add(value);
    }
    
    public String get(String key, int timestamp) {
        if (!store.containsKey(key)) {
            return "";
        }

        int closestTime = 0;
        for (int time : store.get(key).keySet()) {
            // valid time
            if (time <= timestamp) {
                // maximize the time
                closestTime = Math.max(closestTime, time);
            }
        }

        return closestTime == 0 ? "" : store.get(key).get(closestTime).get(store.get(key).get(closestTime).size() - 1);
    }
}
