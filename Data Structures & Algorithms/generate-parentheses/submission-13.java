class Solution {
    void backtrack(int open, int close, StringBuilder s, List<String> res, int n) {
        // we have a solution
        if (open == close && s.length() == 2 * n) {
            res.add(s.toString());
            return;
        }
        
        // can add open parentheses
        if (open < n) {
            s.append('(');
            backtrack(open + 1, close, s, res, n);
            s.deleteCharAt(s.length() - 1);
        }

        // can add close parentheses
        if (close < open) {
            s.append(')');
            backtrack(open, close + 1, s, res, n);
            s.deleteCharAt(s.length() - 1);
        }

    }
    public List<String> generateParenthesis(int n) {
        StringBuilder s = new StringBuilder();
        List<String> res = new ArrayList<>();
        backtrack(0, 0, s, res, n);
        return res;
    }
}
