class Solution {
public:
    unordered_map<int, int> cache;

    int climb(vector<int>& cost, int i) {
        if (i >= cost.size()) {
            return 0;
        }

        if (cache.find(i) != cache.end()) {
            return cache[i];
        }

        cache[i] = cost[i] + min(climb(cost, i + 1), climb(cost, i + 2));
        return cache[i];
    }

    int minCostClimbingStairs(vector<int>& cost) {
        return min(climb(cost, 0), climb(cost, 1));
        
    }
};
