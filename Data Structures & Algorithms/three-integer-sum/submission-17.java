class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int l = i + 1, r = nums.length - 1;
            int target = -nums[i];
            while (l < r) {
                int currSum = nums[l] + nums[r];
                if (currSum == target) {
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                
                // skip duplicates for l and r
                while (l < r && nums[l] == nums[l + 1]) {
                    l++;
                }

                while (l < r && nums[r] == nums[r - 1]) {
                    r--;
                }
                // after l and r are on the last duplicate so inc one more time
                l++;
                r--;
                }
                
                else if (currSum < target) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        return res;
    }
}
