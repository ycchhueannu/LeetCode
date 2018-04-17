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
    int numJewelsInStones(string J, string S) {
        unordered_map<char, bool> hash;
        for (auto& j : J)
            hash[j] = true;
        int ans = 0;
        for (auto& s : S) {
            if (hash[s])
                ans++;
        }
        return ans;
    }
};