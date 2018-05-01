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
    #include <locale> // std::tolower
    string mostCommonWord(string paragraph, vector<string>& banned) {
        char *p_para = new char[paragraph.size()+1];
        strcpy(p_para, paragraph.c_str());
        
        unordered_map<string, int> words;
        unordered_set<string> banSet(banned.begin(), banned.end());
        
        char *ptr = strtok(p_para, " !?',;.");
        while (ptr != NULL) {
            std::string s(ptr);
            for (string::size_type i = 0; i < s.length(); ++i)
                s[i] = std::tolower(s[i]);
            words[s] += 1;
            ptr = strtok(NULL, " !?',;.");
        }
        
        std::pair<string, int> ans = {"", -1};
         
        for (auto w : words) {
            if (banSet.count(w.first) == 0 && w.second > ans.second) {
                ans = {w.first, w.second};
            }
            
        }
        return ans.first;
    }
};