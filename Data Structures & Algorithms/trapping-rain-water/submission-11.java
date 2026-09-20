class Solution {
    public int trap(int[] height) {
        if (height.length == 0) {
            return 0;
        }

        int l = 0, r = height.length - 1;
        int leftMax = height[l], rightMax = height[r];
        int res = 0;

        while (l < r) {
            // the left is the bottleneck
            if (leftMax < rightMax) {
                res += Math.min(leftMax, rightMax) - height[l];
                l++;
                leftMax = Math.max(leftMax, height[l]);
            
            // right is the bottleneck
            } else {
                res += Math.min(leftMax, rightMax) - height[r];
                r--;
                rightMax = Math.max(rightMax, height[r]);
            }
        }
        return res;
    }
}
