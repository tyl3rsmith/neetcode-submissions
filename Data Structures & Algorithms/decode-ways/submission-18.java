class Solution {
    public int dfs(int i, String s) {
        if (i == s.length()) {
            return 1;
        }
        if (s.charAt(i) == '0') {
            return 0;
        }

        // take a single digit
        int res = dfs(i + 1, s);

        // take a double digit
        if (i < s.length() - 1) {
            if (s.charAt(i) == '1' || s.charAt(i) == '2' && s.charAt(i + 1) < '7') {
                res += dfs(i + 2, s);
            }
        }
        return res;
    }

    public int numDecodings(String s) {
        return dfs(0, s);
    }
}
