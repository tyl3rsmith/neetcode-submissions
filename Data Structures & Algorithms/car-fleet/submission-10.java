class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] pairs = new int[position.length][2];
        for (int i = 0; i < position.length; i++) {
            pairs[i] = new int[]{position[i], speed[i]};
        }

        Arrays.sort(pairs, (a, b) -> Integer.compare(b[0], a[0]));
        Stack<Double> stack = new Stack<>();

        for (int[] p : pairs) {
            double timeToDest = (double) (target - p[0]) / p[1];
            if (!stack.isEmpty() && timeToDest <= stack.peek()) {
                continue;
            }
            stack.push(timeToDest);
        }

        return stack.size();

        
    }
}
