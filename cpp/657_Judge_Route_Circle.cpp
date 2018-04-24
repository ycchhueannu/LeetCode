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
    bool judgeCircle(string moves) {
        unordered_map<char, int> h({{'U', 0}, {'D', 0}, {'L', 0}, {'R', 0}});
        for (auto& x : moves)
            ++h[x];
        return (h['U'] == h['D']) && (h['L'] == h['R']);
    }
};