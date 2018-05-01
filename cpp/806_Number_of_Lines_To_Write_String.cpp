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
    vector<int> numberOfLines(vector<int>& widths, string S) {
        int ans = 0;
        int cnt = 0;
        for (int i = 0; i < S.length(); ++i) {
            int wi = widths[S[i]-'a'];
            if (cnt + wi > 100) {
                ++ans;
                cnt = wi;
            }
            else
                cnt += wi;
        }
        if (cnt > 0)
            return {ans+1, cnt};
        else
            return {ans, cnt};
    }
};