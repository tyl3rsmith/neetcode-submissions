class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> mp = new HashMap<>();

        for (int i = 0; i < numbers.length; i++) {
            int complement = target - numbers[i];
            if (mp.containsKey(complement)) {
                return new int[] {mp.get(complement) + 1, i + 1};
            } else {
                mp.put(numbers[i], i);
            }
        }
        return new int[] {-1, -1};
    }
}
