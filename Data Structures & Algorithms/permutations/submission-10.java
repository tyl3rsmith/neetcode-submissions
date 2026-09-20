class Solution {
    private void backtrack(int[] nums, boolean[] used, List<Integer> curr, List<List<Integer>> res) {
        if (curr.size() == nums.length) {
            res.add(new ArrayList<>(curr));
            return;
        }

        // base case: lengths are the same we have a permutation
        for (int i = 0; i < nums.length; i++) {
            // start with this element then backtrack
            if (used[i] == false) {
                curr.add(nums[i]);
                used[i] = true;
                backtrack(nums, used, curr, res);
                curr.remove(curr.size() - 1);
                used[i] = false;
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
