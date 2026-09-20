class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty()) {
            return "";
        }

        Map<Character, Integer> countT = new HashMap<>();
        Map<Character, Integer> window = new HashMap<>();
        for (char c : t.toCharArray()) {
            countT.put(c, countT.getOrDefault(c, 0) + 1);
        }

        int need = countT.size();
        int have = 0;
        
        int[] res = new int[]{-1, -1};
        int resLen = Integer.MAX_VALUE;

        int l = 0;
        for (int r = 0; r < s.length(); r++) {
            // add character to window
            window.put(s.charAt(r), window.getOrDefault(s.charAt(r), 0) + 1);

            // check if there was a match
            if (countT.containsKey(s.charAt(r)) && countT.get(s.charAt(r)) == window.get(s.charAt(r))) {
                have++;
            }

            // while we have a valid window update the res and try to minimize
            while (have == need) {
                if ((r - l + 1) < resLen) {
                    res[0] = l;
                    res[1] = r;
                    resLen = r - l + 1;
                }
                // shrink the window
                window.put(s.charAt(l), window.get(s.charAt(l)) - 1);
                // check if we made a mismatch
                if (countT.containsKey(s.charAt(l)) && countT.get(s.charAt(l)) > window.get(s.charAt(l))) {
                    have--;
                }
                l++;
            }
        }
        return resLen == Integer.MAX_VALUE ? "" : s.substring(res[0], res[1] + 1);
    }
}
