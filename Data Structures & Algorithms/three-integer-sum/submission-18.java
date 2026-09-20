class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            // skip duplicates
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            // two sum with remaining elements
            int target = -nums[i];
            int l = i + 1, r = nums.length - 1;

            // Input: nums = [-4,-1,-1,0,1,2]

            while (l < r) {
                int currSum = nums[l] + nums[r];
                if (currSum < target) {
                    l++;
                } else if (currSum > target) {
                    r--;
                } else {
                    // we found a solution
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));

                    // skip duplicates
                    while (l < r && nums[l] == nums[l + 1]) {
                        l++;
                    }
                    while (l < r && nums[r] == nums[r - 1]) {
                        r--;
                    }

                    l++;
                    r--;
                }
            }
        }
        return res;
    }
}
