class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0, res = 0, max = 0;
        Map<Character, Integer> counts = new HashMap<>();

        for (int r = 0; r < s.length(); r++) {
            // count characters
            if (counts.containsKey(s.charAt(r))) {
                counts.put(s.charAt(r), counts.get(s.charAt(r)) + 1);
            } else {
                counts.put(s.charAt(r), 1);
            }

            // lazily update the max frequency character
            max = Math.max(max, counts.get(s.charAt(r)));

            // fix window if its invalid
            while ((r - l + 1) - max > k) {
                counts.put(s.charAt(l), counts.get(s.charAt(l)) - 1);
                l += 1;
            }

            // update the result
            res = Math.max(res, r - l + 1);
        }


        return res;
        
    }
}
