class Solution {
    private void backtrack(int[] nums, int target, int i, int currentTotal, List<Integer> subset, List<List<Integer>> res) {
        if (currentTotal == target) {
            res.add(new ArrayList<>(subset));
            return;
        }
        if (i >= nums.length) {
            return;
        }

        // include the current num as much as we can
        if (currentTotal + nums[i] <= target) {
            subset.add(nums[i]);
            backtrack(nums, target, i, currentTotal + nums[i], subset, res);
            subset.remove(subset.size() - 1);
        }

        // skip this number
        backtrack(nums, target, i + 1, currentTotal, subset, res);

    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();

        backtrack(nums, target, 0, 0, subset, res);
        return res;
    }

}
