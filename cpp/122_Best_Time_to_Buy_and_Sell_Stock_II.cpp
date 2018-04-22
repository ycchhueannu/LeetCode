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
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int cur = 0; // current transactions
        for (int i = 1; i < prices.size(); ++i) {
            int dif = prices[i] - prices[i-1];
            if (dif >= 0) {
                cur += dif;
            }
            else {
                ans += cur;
                cur = 0;
            }
        }
        ans += cur; // ans may never be updated in loop, e.g. [1, 2, 3, 4, 5]
        return ans;
    }
};