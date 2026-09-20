class Solution {
    void backtrack(int open, int close, List<String> res, int n, StringBuilder s) {
        // base case
        if (open == close && s.length() == 2 * n) {
            res.add(s.toString());
            return;
        }

        // we can add open parentheses
        if (open < n) {
            s.append('(');
            backtrack(open + 1, close, res, n, s);
            s.deleteCharAt(s.length() - 1);
        }

        // we can add close parentheses
        if (close < open) {
            s.append(')');
            backtrack(open, close + 1, res, n, s);
            s.deleteCharAt(s.length() - 1);
        }

    }

    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        StringBuilder s = new StringBuilder();
        backtrack(0, 0, res, n, s);
        return res;
    }
}
