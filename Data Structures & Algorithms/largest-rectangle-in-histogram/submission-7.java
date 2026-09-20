class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<int[]> stack = new Stack<>(); // (index, height)
        int maxArea = 0;

        for (int i = 0; i < heights.length; i++) {
            int start = i;
            while (!stack.isEmpty() && heights[i] < stack.peek()[1]) {
                int[] pair = stack.pop();
                int index = pair[0], height = pair[1];
                maxArea = Math.max(maxArea, height * (i - index));
                start = index;
            }
            stack.push(new int[] {start, heights[i]});
        }

        while (!stack.isEmpty()) {
            int[] pair = stack.pop();
            int index = pair[0], height = pair[1];
            maxArea = Math.max(maxArea, height * (heights.length - index));
        }
        
        return maxArea;
    }
}
