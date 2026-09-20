class Solution {
    boolean isValid(String s) {
        int numOpen = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                numOpen++;
            } else {
                numOpen--;
            }

            if (numOpen < 0) {
                return false;
            }
        }
        
        return numOpen == 0;
    }

    void dfs(String s, List<String> res, int n) {
        if (s.length() == 2 * n) {
            if (isValid(s)) {
                res.add(s);
            }
            return;
        }

        dfs(s + '(', res, n);
        dfs(s + ')', res, n);
    }

    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        dfs("", res, n);
        return res;
    }
}
