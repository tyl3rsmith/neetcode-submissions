class Solution {
    public int trap(int[] height) {
        if (height.length < 1) {
            return 0;
        }

        int[] leftMax = new int[height.length];
        int[] rightMax = new int[height.length];

        leftMax[0] = height[0];
        for (int l = 1; l < height.length; l++) {
            leftMax[l] = Math.max(leftMax[l - 1], height[l]);
        }

        rightMax[height.length - 1] = height[height.length - 1];
        for (int r = height.length - 2; r >= 0; r--) {
            rightMax[r] = Math.max(rightMax[r + 1], height[r]);
        }

        int res = 0;
        for (int i = 0; i < height.length; i++) {
            res += Math.min(leftMax[i], rightMax[i]) - height[i];
        }
        return res;
    }
}
