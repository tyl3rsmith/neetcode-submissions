class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        int res = 0;

        Set<Character> chars = new HashSet<>();
        for (int r = 0; r < s.length(); r++) {
            // make the window valid
            while (chars.contains(s.charAt(r))) {
                chars.remove(s.charAt(l));
                l++;
            }

            // update the window and result
            chars.add(s.charAt(r));
            res = Math.max(res, r - l + 1);
        }

        return res;
    }
}
