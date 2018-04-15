/*
// Employee info
class Employee {
public:
    // It's the unique ID of each node.
    // unique id of this employee
    int id;
    // the importance value of this employee
    int importance;
    // the id of direct subordinates
    vector<int> subordinates;
};
*/
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
    int getImportance(vector<Employee*> employees, int id) {
        // ID may not in 0~2000
        unordered_map<int, int> h_visit; // hash, for visit look up in BFS
        unordered_map<int, int> h_val; // hash, for importance value look up
        unordered_map<int, vector<int> > h_sub; // hash, for subordinate look up
        for (int i = 0; i < employees.size(); ++i) {
            h_visit[employees[i]->id] = 0; // not visit
            h_val[employees[i]->id] = employees[i]->importance;
            h_sub[employees[i]->id] = employees[i]->subordinates;
        }
        
        queue<int> q;
        q.push(id);
        int total = 0;
        while (!q.empty()) {
            int cur = q.front(); // current employee
            q.pop();
            h_visit[cur] = 1;
            total += h_val[cur];
            for (int i = 0; i < h_sub[cur].size(); ++i) {
                int adj = h_sub[cur][i]; // adj is the subordinate of cur
                if (!h_visit[adj]) {
                    q.push(adj);
                }
            } // end for
        } // end while
        return  total;
    }
};