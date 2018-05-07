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
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1)
            return 0;
        int start = 0, end = 0;
        int ans = 0;
        int p = 1; // product
        for (; end < nums.size(); ++end) {
            p *= nums[end];
            while (p >= k) {
                p /= nums[start++];
            }
            ans += end - start + 1;
        }
        return ans;
    }
};