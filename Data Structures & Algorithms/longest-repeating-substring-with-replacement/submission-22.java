class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0;

        for (int i = 0; i < s.length(); i++) {
            int maxf = 0;
            Map<Character, Integer> counts = new HashMap<>();

            for (int j = i; j < s.length(); j++) {
                if (counts.containsKey(s.charAt(j))) {
                    counts.put(s.charAt(j), counts.get(s.charAt(j)) + 1);
                } else {
                    counts.put(s.charAt(j), 1);
                }

                maxf = Math.max(maxf, counts.get(s.charAt(j)));

                if ((j - i + 1) - maxf <= k) {
                    res = Math.max(res, j - i + 1);
                } else {
                    break;
                }
            }
        }
        return res;
    }
}
