class Solution {
    public int climb(int i, int n, Map<Integer, Integer> memo) {
        if (i == n) {
            return 1;
        }
        if (i > n) {
            return 0;
        }

        if (memo.containsKey(i)) {
            return memo.get(i);
        }

        memo.put(i, climb(i + 1, n, memo) + climb(i + 2, n, memo));
        return memo.get(i);
    }

    public int climbStairs(int n) {
        Map<Integer, Integer> memo = new HashMap<>();
        return climb(0, n, memo);
    }
}
