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
    string longestWord(vector<string>& words) {
        #include <algorithm> // std::sort
        unordered_set<string> hash;
        string ans = "";
        
        sort(words.begin(), words.end());
        for(auto& str : words) {
            // if str = "abcd", then "abc" must be in hash (this is what the second condition does)
            if( str.size() == 1 || hash.count(str.substr(0, str.size()-1))) { // count() return 1 if found
                hash.insert(str);
                if(str.size() > ans.size())
                    ans = str;
            } // end if
        }
        return ans;
    }
};