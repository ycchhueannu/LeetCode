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
    vector<string> ans;
    
    void DFS(unordered_map<string, forward_list<string>>& adjList, string cur) {
        while (!adjList[cur].empty()) {
            string next = adjList[cur].front();
            adjList[cur].pop_front();
            DFS(adjList, next);
        }
        ans.push_back(cur);
        return;
    }
    
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        #include <algorithm> // std::reverse
        unordered_map<string, forward_list<string>> adjList;
        for (auto t : tickets)
            adjList[t.first].push_front(t.second);
        for (auto x : adjList) // sort(x.second.begin(), x.second.end()) is wrong
            adjList[x.first].sort();
            
        // do Best-First-Search (DFS-like, we already sort destination airport in adjList)
        DFS(adjList, "JFK");
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
// [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] should return
// ["JFK","NRT","JFK","KUL"], not ["JFK","KUL"]