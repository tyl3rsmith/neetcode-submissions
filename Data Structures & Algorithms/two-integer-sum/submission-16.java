class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[][] A = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++) {
            A[i][0] = nums[i];
            A[i][1] = i;
        }

        Arrays.sort(A, Comparator.comparingInt(a -> a[0]));

        int l = 0;
        int r = A.length - 1;

        while (l < r) {
            int curr = A[l][0] + A[r][0];

            if (curr == target) {
                int idx1 = Math.min(A[l][1], A[r][1]);
                int idx2 = Math.max(A[l][1], A[r][1]);
                return new int[]{idx1, idx2};

            } else if (curr < target) {
                l++;

            } else {
                r--;
            }
        }

    return new int[]{-1, -1};
    }
}
