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
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        // note that all points have coordinates with absolute value <= 10000
        // no need to worry about overflow
        int d = abs(target[0]) + abs(target[1]); // start point at (0, 0)
        for (auto& g : ghosts) {
            if (abs(g[0]-target[0]) + abs(g[1]-target[1]) <= d)
                return false;
        }
        return true;
    }
};