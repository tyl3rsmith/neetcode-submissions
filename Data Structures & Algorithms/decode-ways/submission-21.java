class Solution {
    public int numDecodings(String s) {
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(s.length(), 1);

        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '0') {
                dp.put(i, 0);
            } else {
                dp.put(i, dp.get(i + 1));
            }

            if (i + 1 < s.length()) {
                if (s.charAt(i) == '1' || s.charAt(i) == '2' && s.charAt(i + 1) < '7') {
                    dp.put(i, dp.get(i + 1) + dp.get(i + 2));
                }
            }
        }
        return dp.get(0);
    }
}
