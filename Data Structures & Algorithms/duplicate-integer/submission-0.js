class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const a = new Set();
        for (const num of nums) {
            if (a.has(num)) {
                return true;
            }
            a.add(num);
        }
        return false;
    }
}
