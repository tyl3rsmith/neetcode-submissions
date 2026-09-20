class Solution {
    public int trap(int[] height) {
        if (height.length < 3) {
            return 0;
        }

        int[] leftMax = new int[height.length];
        int[] rightMax = new int[height.length];

        leftMax[0] = 0;
        leftMax[1] = height[0];
        for (int l = 2; l < height.length; l++) {
            leftMax[l] = Math.max(leftMax[l - 1], height[l - 1]);
        }

        rightMax[height.length - 1] = 0;
        rightMax[height.length - 2] = height[height.length - 1];
        for (int r = height.length - 3; r >= 0; r--) {
            rightMax[r] = Math.max(rightMax[r + 1], height[r + 1]);
        }

        int res = 0;
        for (int i = 0; i < height.length; i++) {
            int currArea = Math.min(leftMax[i], rightMax[i]) - height[i];
            if (currArea > 0) {
                res += currArea;
            }
        }
        return res;
    }
}
