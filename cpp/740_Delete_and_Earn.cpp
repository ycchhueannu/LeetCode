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
    int deleteAndEarn(vector<int>& nums) {
        #define ELT_MAX (int)1e4
        int b[ELT_MAX+5] = {0}; // bucket
        int max_num = -1;
        /* [2, 3, 3, 3, 4, 4] -> [0, 0, 2, 9, 8, 0, ..] */
        for (auto &x: nums) {
            b[x] += x;
            max_num = max(max_num, x);
        }
        // case i == 1
        int pick_i = b[1];
        int notPick_i = b[0];
        for (int i = 2; i <= max_num; ++i) {
            //int taken = b[i] + notPick_i;
            int noTaken = max(pick_i, notPick_i);
            pick_i = b[i] + notPick_i; // taken
            notPick_i = noTaken;
        }
        
        return max(pick_i, notPick_i);
    }
};