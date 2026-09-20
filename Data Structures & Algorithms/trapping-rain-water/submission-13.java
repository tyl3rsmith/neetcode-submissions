class Solution {
    public int trap(int[] height) {
        if (height.length == 0) {
            return 0;
        }

        int l = 0, r = height.length - 1;
        int leftMax = height[l], rightMax = height[r];
        int res = 0;

        while (l < r) {
            leftMax = Math.max(leftMax, height[l]);
            rightMax = Math.max(rightMax, height[r]);
            // idea: always shift the bottle neck pointer
            // water = min(max(l), max(r)) - height
            // since we are taking the min it doesn't matter how big the other can get

            if (leftMax < rightMax) {
                // the bottleneck is the left height
                // calculate how much water we can trap here then shift the left ptr
                res += leftMax - height[l];
                l++;
            } else {
                res += rightMax - height[r];
                r--;
            }
        }
        return res;
    }
}
