class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> perms = Arrays.asList(new ArrayList<>());

        for (int num : nums) {
            List<List<Integer>> res = new ArrayList<>();
            for (List<Integer> p : perms) {
                for (int i = 0; i <= p.size(); i++) {
                    List<Integer> p_copy = new ArrayList<>(p);
                    p_copy.add(i, num);
                    res.add(p_copy);
                }
            }
            perms = res;
        }

        return perms;
    }
}
