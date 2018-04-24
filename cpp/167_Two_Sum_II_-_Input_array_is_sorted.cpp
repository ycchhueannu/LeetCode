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
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0, end = numbers.size()-1;
        while (start < end) {
            if (numbers[start] + numbers[end] == target) {
                vector<int> ans = {start+1, end+1}; // not zero-based
                return ans;
            }
            else if (numbers[start] + numbers[end] > target)
                --end;
            else
                ++start;
        }
    }
};