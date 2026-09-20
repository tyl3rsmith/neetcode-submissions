class Solution {
    private void backtrack(int[] candidates, int target, int total, int i, List<Integer> current, List<List<Integer>> res) {
        if (total == target) {
            res.add(new ArrayList<>(current));
            return;
        }

        if (total > target || i >= candidates.length) {
            return;
        }

        // use this candidate
        current.add(candidates[i]);
        backtrack(candidates, target, total + candidates[i], i + 1, current, res);
        current.remove(current.size() - 1);

        // skip duplicates
        while (i < candidates.length - 1 && candidates[i] == candidates[i + 1]) {
            i++;
        }

        // do not include this candidate
        backtrack(candidates, target, total, i + 1, current, res);
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(candidates, target, 0, 0, current, res);
        return res;    
    }
}
