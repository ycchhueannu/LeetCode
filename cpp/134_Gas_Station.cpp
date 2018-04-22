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
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        long long int sum = 0;
        long long int remain = 0; // remaining gas in tank
        int start = 0;
        for (int i = 0; i < gas.size(); ++i) {
            int cur = gas[i] - cost[i];
            sum += cur;
            remain += cur;
            if (remain < 0) {
                start = i + 1; // seek for the next position
                remain = 0; // reset tank
            }
        } // end for
        if (sum < 0)
            return -1;
        return start;
    }
};