class Solution {
    public int dfs(int i, String s, int[] memo) {
        if (memo[i] != -1) {
            return memo[i];
        }
        if (s.charAt(i) == '0') {
            return 0;
        }

        // take a single digit
        int res = dfs(i + 1, s, memo);

        // take a double digit
        if (i < s.length() - 1) {
            if (s.charAt(i) == '1' || s.charAt(i) == '2' && s.charAt(i + 1) < '7') {
                res += dfs(i + 2, s, memo);
            }
        }
        memo[i] = res;
        return res;
    }

    public int numDecodings(String s) {
        int[] memo = new int[s.length() + 1];
        for (int i = 0; i < memo.length; i++) {
            memo[i] = -1;
        }
        memo[s.length()] = 1;

        return dfs(0, s, memo);
    }
}
