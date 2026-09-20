class Solution {
    public int trap(int[] height) {
        int res = 0;
        
        for (int i = 0; i < height.length; i++) {
            int leftMax = height[i], rightMax = height[i];

            for (int l = 0; l < i; l++) {
                leftMax = Math.max(leftMax, height[l]);
            }

            for (int r = i + 1; r < height.length; r++) {
                rightMax = Math.max(rightMax, height[r]);
            }

            int currAmt = Math.min(leftMax, rightMax) - height[i];
            res += currAmt;
        }
        return res;
    }
}
