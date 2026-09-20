class Solution {
    public int dfs(int i, String s, Map<Integer, Integer> memo) {
        if (i == s.length()) {
            return 1;
        }
        if (s.charAt(i) == '0') {
            return 0;
        }

        if (memo.containsKey(i)) {
            return memo.get(i);
        }

        int res = dfs(i + 1, s, memo);

        if (i < s.length() - 1) {
            if (s.charAt(i) == '1' || s.charAt(i) == '2' && s.charAt(i + 1) < '7') {
                res += dfs(i + 2, s, memo);
            }
        }

        memo.put(i, res);
        return res;
    }
    public int numDecodings(String s) {
        Map<Integer, Integer> memo = new HashMap<>();
        return dfs(0, s, memo);
    }
}
