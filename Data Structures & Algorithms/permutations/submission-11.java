class Solution {
    private void backtrack(int[] nums, boolean[] used, List<Integer> curr, List<List<Integer>> res) {
        if (curr.size() == nums.length) {
            res.add(new ArrayList<>(curr));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i] == false) {
                curr.add(nums[i]);
                used[i] = true;
                backtrack(nums, used, curr, res);
                used[i] = false;
                curr.remove(curr.size() - 1);
            } else {
                continue;
            }
        }

    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, used, curr, res);
        return res;
    }
}
