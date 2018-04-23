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
    int majorityElement(vector<int>& nums) {
        long long int threshold = nums.size() / 2;
        unordered_map<int, int> hash;
        for (const auto& x : nums) {
            if (++hash[x] > threshold)
                return x;
        }
    }
};
// see also: https://leetcode.com/problems/majority-element/discuss/51612/6-Suggested-Solutions-in-C++-with-Explanations