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
    #include <cstddef> // std::size_t
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        unordered_map<string, int> h; // hash
        for (string s : cpdomains) {
            // convert string to *char
            char *cptr = new char [s.length()+1];
            strcpy (cptr, s.c_str());
            
            // parse token ("50 yahoo.com" -> [50 yahoo com])
            vector<string> vec_substr;
            char *substr = strtok(cptr, " .");
            while (substr != NULL) {
                //cout << substr << " ";
                vec_substr.push_back(substr);
                substr = strtok(NULL, " .");
            }
            //cout << "\n";
            
            int num = stoi(vec_substr[0]);
            for (int i = 1; i < vec_substr.size(); ++i) {
                string key = "";
                for (int j = i; j < vec_substr.size(); ++j) {
                    key += vec_substr[j] + ".";
                }
                key.pop_back(); // remove the last '.'
                //cout << key << " " << num << "\n";
                h[key] += num;
            }
        }
        
        vector<string> ans;
        for (auto& it : h) {
            ans.push_back(to_string(it.second) + " " + it.first);
        }
        
        return ans;
    }
};