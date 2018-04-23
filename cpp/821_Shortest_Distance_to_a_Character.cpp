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
    vector<int> shortestToChar(string S, char C) {
        vector<int> ans(S.size(), -1);
        vector<int> c; // note that the first and the last are dummy
        c.push_back(0); // dummy
        for (int i = 0; i < S.size(); ++i) {
            if (S[i] == C)
                c.push_back(i);
        }
        c.push_back(S.size()-1); // dummy
        
        // c[0..n+1] = [0, c1, c2, c3, ..., cn, S.size()], size = n+2, valid indexes are 1..n
        for (int i = 1; i < c.size() - 1; ++i) {
            int dist;
            ans[ c[i] ] = 0;
            // span left
            for (int idx=c[i]-1, dist=1; idx >= c[i-1]; --idx, ++dist) {
                //assert(idx >= 0 && idx < S.size());
                if (i == 1)
                    ans[idx] = dist;
                else if (dist <= idx - c[i-1])
                    ans[idx] = dist;
                else
                    break;
            }
            // span right
            for (int idx=c[i]+1, dist=1; idx <= c[i+1]; ++idx, ++dist) {
                //assert(idx >= 0 && idx < S.size());
                if (i == c.size()-2)
                    ans[idx] = dist;
                else if (dist <= c[i+1] - idx)
                    ans[idx] = dist;
                else
                    break;
            }
            
        } // end for
        
        return ans;
    }
};