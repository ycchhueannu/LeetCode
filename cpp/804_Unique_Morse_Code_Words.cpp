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
    int uniqueMorseRepresentations(vector<string>& words) {
        unordered_map<char, string> h( { {'a',".-"}, {'b',"-..."}, {'c',"-.-."}, \
            {'d',"-.."}, {'e',"."}, {'f',"..-."}, {'g',"--."}, {'h',"...."}, \
            {'i',".."}, {'j',".---"}, {'k',"-.-"}, {'l',".-.."}, {'m',"--"}, \
            {'n',"-."}, {'o',"---"}, {'p',".--."}, {'q',"--.-"}, {'r',".-."}, \
            {'s',"..."}, {'t',"-"}, {'u',"..-"}, {'v',"...-"}, {'w',".--"}, \
            {'x',"-..-"}, {'y',"-.--"}, {'z',"--.."} } );
        unordered_set<string> set;
        for (auto& w : words) {
            string s;
            for (auto& c : w)
                s += h[c];
            set.insert(s);
        } // end for
        return set.size();
    }
};