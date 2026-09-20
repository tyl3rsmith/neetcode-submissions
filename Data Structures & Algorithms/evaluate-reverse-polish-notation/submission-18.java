class Solution {
    public int evalRPN(String[] tokens) {
        return dfs(new ArrayList<>(Arrays.asList(tokens)));
    }

    private int dfs(List<String> tokenList) {
        String token = tokenList.remove(tokenList.size() - 1);

        // this is an operand
        if (!"+-*/".contains(token)) {
            return Integer.parseInt(token);
        }

        // this is an operator
        // we need two operands
        int right = dfs(tokenList);
        int left = dfs(tokenList);

        switch (token) {
            case "+":
                return left + right;
            case "-":
                return left - right;
            case "*":
                return left * right;
            case "/":
                return left / right;
        }

        return 0;
    }
}

