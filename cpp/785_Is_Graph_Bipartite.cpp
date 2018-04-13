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
    #define RED 0
    #define BLACK 1

    bool isBipartite(vector<vector<int>>& graph) {
        int sz = graph.size();
        
        int Visit[sz] = {0};
        unordered_map<int, int> color;
        for (int i = 0; i < sz; ++i) {
            queue<int> q;
            if ( !Visit[i] ) {
                q.push(i);
                int flag = 0; // flip color
                while (!q.empty()) {
                    int parent = q.front();
                    q.pop();
                    Visit[parent] = 1;   
                    if (color.find(parent) == color.end()) { // only not found can draw color
                        if (flag % 2) { color[parent] = RED; }
                        else { color[parent] = BLACK; }
                    }
                    //printf("parent: %d, color=%d\n", parent, color[parent]);

                    for (int i = 0; i < graph[parent].size(); ++i) {
                        int adj = graph[parent][i];
                        
                        if (Visit[adj]) {
                            if (color[adj] == color[parent]) return false;
                            continue;
                        }
                        
                        q.push(adj);

                        if (color[parent] == RED) { color[adj] = BLACK; }
                        else { color[adj] = RED; }
                        Visit[adj] = 1; // add this will run A LOT FASTER
                    } // end for

                    ++flag;
                    
                } // end while (!q.empty())
                
            } // end if
            
        } // end for
        return true;
    }
};