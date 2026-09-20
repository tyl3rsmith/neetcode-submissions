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
        int closestTime = 0;

        for (int i = 0; i < store.get(key).size(); i++) {
            int time = Integer.parseInt(store.get(key).get(i).get(0));

            if (time <= timestamp && time > closestTime) {
                resIdx = i;
                closestTime = time;
            }
        }

        return resIdx == -1 ? "" : store.get(key).get(resIdx).get(1);
        
    }
}
