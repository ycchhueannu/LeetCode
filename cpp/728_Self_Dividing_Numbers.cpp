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
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ans;
        for (int num = left; num <= right; ++num) {
            int isDivisible = 1;
            for (int remain = num; remain != 0; remain /= 10) {
                int digit = remain % 10;
                if ((digit == 0) || (num % digit != 0)) {
                    isDivisible = 0;
                    break;
                }
            }
            if (isDivisible)
                ans.push_back(num);
        }
        return ans;
    }
};