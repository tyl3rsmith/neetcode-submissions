class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        int n = heights.length;

        for (int i = 0; i < n; i++) {
            int height = heights[i];

            int leftMax = i;
            while (leftMax >= 0 && heights[leftMax] >= height) {
                leftMax--;
            }

            int rightMax = i + 1;
            while (rightMax < n && heights[rightMax] >= height) {
                rightMax++;
            }

            // over shot by one
            leftMax++;
            rightMax--;

            maxArea = Math.max(maxArea, height * (rightMax - leftMax + 1));
        }

        return maxArea;
        
    }
}
