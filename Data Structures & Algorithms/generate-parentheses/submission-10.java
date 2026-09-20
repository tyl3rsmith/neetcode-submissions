class Solution {
    private static boolean valid(String s) {
        int numOpen = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                numOpen++;
            } else {
                numOpen--;
            }

            // if closed exceeds open it cant be valid
            if (numOpen < 0) {
                return false;
            }
        }
        // if numOpen isn't 0 then the parentheses were not closed properly
        return numOpen == 0;

    }

    private static void dfs(String s, List<String> res, int n) {
        if (2 * n == s.length()) {
            if (Solution.valid(s)) {
                res.add(s);
            }
            return;
        }
        Solution.dfs(s + '(', res, n);
        Solution.dfs(s + ')', res, n);
    }

    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        Solution.dfs("", res, n);
        return res;
    }
}
