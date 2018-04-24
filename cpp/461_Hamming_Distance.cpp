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
    #include <bitset>
    int hammingDistance(int x, int y) {
        string sx = std::bitset<32> (x).to_string();
        string sy = std::bitset<32> (y).to_string();
        int ans = 0;
        for (int i = 0; i < 32; ++i) {
           if (sx[i] != sy[i])
               ++ans;
        }
        return ans;
    }
};
/*
unsigned int r = x ^ y;
        int b = 0;
        while(r) {
            if(r & 1) b++;
            r = (r >> 1);
        }
        return b;
*/