class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        // sorted word -> anagrams
        Map<String, List<String>> anagramMap = new HashMap<>();

        for (String s : strs) {
            // use the sorted word as the key 
            char[] sChars = s.toCharArray();
            Arrays.sort(sChars);
            String sortedS = new String(sChars);

            // append each word with the same sorted word
            if (anagramMap.containsKey(sortedS)) {
                anagramMap.get(sortedS).add(s);
            } else {
                anagramMap.put(sortedS, new ArrayList<>(Arrays.asList(s)));
            }
        }
        
        // for each key add its list to a result list
        for (Map.Entry<String, List<String>> entry : anagramMap.entrySet()) {
            res.add(entry.getValue());
        }

        return res;
    }
}
