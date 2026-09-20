class TimeMap {
    private Map<String, List<List<String>>> store;

    public TimeMap() {
        store = new HashMap<>();   
    }
    
    public void set(String key, String value, int timestamp) {
        if (!store.containsKey(key)) {
            store.put(key, new ArrayList<>());
        }
        store.get(key).add(Arrays.asList(value, Integer.toString(timestamp)));
    }
    
    public String get(String key, int timestamp) {
        if (!store.containsKey(key)) {
            return "";
        }

        int l = 0, r = store.get(key).size() - 1;
        int resIdx = -1;

        while (l <= r) {
            int m = l + (r - l) / 2;
            int time = Integer.parseInt(store.get(key).get(m).get(1));

            if (time == timestamp) {
                resIdx = m;
                break;
            } else if (time < timestamp) { // potential result, try to maximize looking right
                resIdx = m;
                l = m + 1;
            } else { // time is too large need to look left for smaller one
                r = m - 1;
            }
        }

        return (resIdx == -1) ? "" : store.get(key).get(resIdx).get(0);

    }
}
