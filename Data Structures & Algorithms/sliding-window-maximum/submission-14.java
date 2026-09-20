class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] res = new int[nums.length - k + 1];
        Deque<Integer> d = new LinkedList<>();
        int l = 0;

        for (int r = 0; r < nums.length; r++) {
            while (!d.isEmpty() && nums[r] > nums[d.getLast()]) {
                d.removeLast();
            }
            d.addLast(r);

            if (l > d.getFirst()) {
                d.removeFirst();
            }

            if (r + 1 >= k) {
                res[l] = nums[d.getFirst()];
                l++;
            }

        }

        return res;
    }
}
