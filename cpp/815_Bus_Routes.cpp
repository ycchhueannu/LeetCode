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
    #define STOP_ID int
    #define BUS_ID int
    void debugAdjList(unordered_map<STOP_ID, unordered_set<BUS_ID> >& adjList) {
        for (auto& it : adjList) {
            std::cout << "stop #" << it.first << " contains bus id:";
            for (auto& p : it.second) {
                printf("%d ", p);
            }
            printf("\n");
        }
    } 
    void processData(vector<vector<int>>& routes, unordered_map<STOP_ID, unordered_set<BUS_ID> >& adjList) {
        for (int i = 0; i < routes.size(); ++i) { // i is current bus id
            for (int j = 0; j < routes[i].size(); ++j) {
                int cur_stop = routes[i][j];
                adjList[cur_stop].insert(i);
            } // end for (j)
        } // end for (i)
        return;
    }
    int numBusesToDestination(vector<vector<int>>& routes, int S, int T) {
        if (S == T)
            return 0;
        
        unordered_map<STOP_ID, unordered_set<BUS_ID> > adjList; // though it's neither list nor vector..
        unordered_set<int> visit; // note that unorder_set and unordered_map both ave. and worst time are the same
        processData(routes, adjList); // pass reference
        //debugAdjList(adjList);

        queue<STOP_ID> q;
        queue<int> q_numS; // number of stops
        q.push(S);
        q_numS.push(0);
        visit.insert(S);
        
        while (!q.empty()) {
            int cur_stop = q.front(); q.pop();
            int cur_numS = q_numS.front(); q_numS.pop();
            if (cur_stop == T) {
                return cur_numS;
            }
            for (auto& adj_bus : adjList[cur_stop]) {
                for (auto& x : routes[adj_bus]) {
                    if (visit.find(x) == visit.end()) {
                        visit.insert(x);
                        q.push(x);
                        q_numS.push(cur_numS+1);
                    }
                }
                routes[adj_bus].clear();
            } // end for  
        } // end while
        return -1;
    }
};

// unordered_map<int, unordered_map<int, int>> getBusID; // getBusID[from][to] = bus id. THIS METHOD IS
// DISCARD, since may have duplicate bus ids on the same routes, which loss simplicity for fast look up

// My previous method is to make adjcency list s.t. vector is bus stop, and it's neighbor is pair, which
// records next bus stop and bus id, e.g. if routes = [[1, 2, 7], [3, 6, 7]] looks like:
// 1 -> (2, 0)
// 2 -> (7, 0)
// 3 -> (6, 1)
// 6 -> (7, 1)
// 7 -> (1, 0) -> (3, 1)
// and visit is a hash function convert from_stop, to_stop, busID into string, e.g. "1 2 0" means at stop1
// go to stop2 by bus0, and we can run original BFS. However, this has a major flaw, if the test cases are
// routes [[78, 97, 99, 102, 143, 180], [78, 102]], S = 180, T = 143, then you can just see the answer is
// 1 (travel by bus0), but this algorithm will first goto 78, and take bus1 forward to stop102, and then
// reach 143, which eventually output 3, and since "102 143 0" this route is marked as visited, the route
// 180->78->97->...(only takes one bus) will stuck at 102 and then terminates (I tried to fix this by add
// bidirectional link in every buses when initializing, but got TLE)
/*
      ----------------------------
     /                            \
    78------->97------->99------->102------->143------->180
    ^                                                    |
    |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |

*/