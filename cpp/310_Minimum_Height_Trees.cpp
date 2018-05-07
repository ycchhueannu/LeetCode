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
    void BFS(const int start, const vector<vector<int> >& adjList, bool backTrack, vector<int>& parent, int& v1, int& d1) {
        int n = adjList.size();
        vector<bool> notVisit(n, true);

        queue<int> qn, qd; // queue vertex, distance
        qn.push(start);
        qd.push(0);
        while (!qn.empty()) {
            int cur = qn.front(); qn.pop();
            int dist = qd.front(); qd.pop();
            notVisit[cur] = false;
            int next_dist = dist+1; // avoid compute "dist+1" many times
            for (auto& adj : adjList[cur]) {
                if (notVisit[adj]) {
                    qn.push(adj);
                    qd.push(next_dist);
                    if (backTrack)
                        parent[adj] = cur;
                    v1 = adj;
                    d1 = next_dist;
                }
            }
        }
        return;
    }
    
    vector<int> backTrack(const int start, const int diameter, const vector<int>& parent) {
        int length = 0;
        vector<int> ret;
        if (diameter % 2) { // odd, has two solutions
            int len1 = diameter / 2;
            int len2 = len1 + 1; // diameter/2 + 1
            for (int cur = start; cur != -1; cur = parent[cur]) {
                if (length == len1 || length == len2)
                    ret.push_back(cur);
                ++length;
            }
        }
        else { // even, has one solution
            int len1 = diameter / 2;
            for (int cur = start; cur != -1; cur = parent[cur]) {
                if (length == len1)
                    ret.push_back(cur);
                ++length;
            }
        }
        return ret;
    }
    
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
        if (n == 1)
            return {0};
        vector<vector<int>> adjList(n);
        // construct adjacency list
        for (auto& e : edges) {
            adjList[e.first].push_back(e.second);
            adjList[e.second].push_back(e.first);
        }
        // find 'diameter' of the tree, you can google if don't know how to find
        vector<int> parent(n, -1); // for backtracking

        int far_v1 = -1, far_d1 = -1;
        // pick arbitrary vectex(0), do BFS record farthest vectex (arbitrary one)
        BFS(0, adjList, false, parent, far_v1, far_d1);
        
        int far_v2 = -1, far_d2 = -1;
        // pick farthest vectex record so far, do BFS record another one
        BFS(far_v1, adjList, true, parent, far_v2, far_d2);

        //printf("%d %d\n", far_v1, far_v2);
        //int diameter = far_d2;
        
        vector<int> ans;       
        ans = backTrack(far_v2, far_d2, parent);
        
        return ans;
    }
};