class Solution {
public:
    unordered_map<int, int> cache;
    
    int dfs(vector<int>& nums, int i) {
        if (i >= nums.size()) {
            return 0;
        }
        if (cache.find(i) != cache.end()) {
            return cache[i];
        }

        int robCurr = nums[i] + dfs(nums, i + 2);
        int skipCurr = dfs(nums, i + 1);

        cache[i] = max(robCurr, skipCurr);
        return cache[i];
    }

    int rob(vector<int>& nums) {
        return dfs(nums, 0);
    }
};
