class Solution {
    public int dfs(int i, String s, Map<Integer, Integer> memo) {
        // base case or already cached
        if (memo.containsKey(i)) {
            return memo.get(i);
        }
        // string starts with 0, its invalid
        if (s.charAt(i) == '0') {
            return 0;
        }

        // subproblem #1
        int res = dfs(i + 1, s, memo);

        // subproblem #2
        if (i + 1 < s.length()) {
            if (s.charAt(i) == '1' || s.charAt(i) == '2' && s.charAt(i + 1) < '7') {
                res += dfs(i + 2, s, memo);
            }
        }

        memo.put(i, res);
        return res;
    }

    public int numDecodings(String s) {
        Map<Integer, Integer> memo = new HashMap<>();
        memo.put(s.length(), 1);
        return dfs(0, s, memo);
    }
}
