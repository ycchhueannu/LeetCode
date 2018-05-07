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
    #define PAIR pair<string, int>
    class myPairComp {
        // sorted by frequency, if two words have the same frequency,
        // the word with the lower alphabetical order comes first
        public:
            bool operator() (const PAIR lhs, const PAIR rhs)
                { return (lhs.second < rhs.second) || (lhs.second == rhs.second && lhs.first > rhs.first); }
    };
    
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> h;
        for (auto w : words)
            ++h[w];
        priority_queue<PAIR, vector<PAIR>, myPairComp> pq(h.begin(), h.end());
        vector<string> ans;

        int cnt = 0;
        while (!pq.empty() && cnt < k) {
            ans.push_back((pq.top()).first);
            pq.pop();
            ++cnt;
        }
        return ans;
    }
};