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
    bool validPalindrome(string s) {
        bool res1 = true, res2 = true;
        
        int low = 0, high = s.length()-1, canChange = 1;
        while (low < high) {
            if (s[low] != s[high]) {
                if (!canChange) { res1 = false; break; }
                canChange = 0;
                // different in this if-statement
                if (s[low+1] == s[high]) ++low;
                else --high;
            }
            else { ++low; --high; }
        }
        
        low = 0; high = s.length()-1; canChange = 1;
        while (low < high) {
            if (s[low] != s[high]) {
                if (!canChange) { res2 = false; break; }
                canChange = 0;
                // different in this if-statement
                if (s[high-1] == s[low]) --high;
                else ++low;
            }
            else { ++low; --high; }
        }
        
        return res1 || res2;
    }
};
// think about how to deal with "lcxyyxcxl", in this string
// we should delete right-most x, but how do you determine which
// character should be deleted?