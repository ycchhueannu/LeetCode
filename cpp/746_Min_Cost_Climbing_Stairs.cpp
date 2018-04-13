// how to get Leetcode tests to run approximately 10-40% faster, since they do a lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int sz = cost.size();
        if (sz <= 2) {
            return min(cost[0], cost[1]);
        }
        else {
            for (int i = 2; i < sz; ++i) {
                cost[i] += min(cost[i-1], cost[i-2]);
            }
        }
        return min(cost[sz-1], cost[sz-2]);
    }
};