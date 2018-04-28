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
    #define ITEM_TYPE std::pair<int, std::pair<int, int> >
    class itemTypeComp {
    public:
        bool operator() (const ITEM_TYPE lhs, const ITEM_TYPE rhs) { return lhs.first > rhs.first; }
    };
    
    int swimInWater(vector<vector<int>>& grid) {
        const int N = grid.size(); // assert (N == grid[0].size());
        priority_queue<ITEM_TYPE, vector<ITEM_TYPE>, itemTypeComp> minPQ;
        int elapseTime = -1; // assume all time >= 0
        minPQ.push( { grid[0][0], {0, 0} } );
        
        //vector<bool> tmp(grid[0].size(), true);
        //vector<vector<bool>> notVisit(grid.size(), tmp);
        vector<vector<bool>> notVisit(N, vector<bool>(N, true));
        while (!minPQ.empty()) {
            ITEM_TYPE cur = minPQ.top();
            minPQ.pop();
            int num = cur.first;
            int x = (cur.second).first;
            int y = (cur.second).second;
            elapseTime = max(elapseTime, grid[x][y]);
            notVisit[x][y] = false;
            if ((x == y) && (x == N-1)) // reach right bottom
                return elapseTime;
            
            // 'BFS' (Best First Search) traverse
            if (x > 0 && notVisit[x-1][y]) { // can up
                minPQ.push( {grid[x-1][y], {x-1, y}} );
                notVisit[x-1][y] = false;
            }
            if (x < N-1 && notVisit[x+1][y]) { // can down
                minPQ.push( {grid[x+1][y], {x+1, y}} );
                notVisit[x+1][y] = false;
            }
            if (y > 0 && notVisit[x][y-1]) { // can left
                minPQ.push( {grid[x][y-1], {x, y-1}} );
                notVisit[x][y-1] = false;
            }
            if (y < N-1 && notVisit[x][y+1]) { // can right
                minPQ.push( {grid[x][y+1], {x, y+1}} );
                notVisit[x][y+1] = false;
            }
            
        } // end while

        return -1; // should never be here
    }
};

// Naive Solution: mark max number as unreachable, do DFS to test if can reach
// end, decrement the number and then repeat until can not. Time: O(n^4), since
// there are O(n^2) nodes, and each DFS takes O(V+E) = O(n^2+ 4*n^2) = O(n^2)

// Improvement: use binary search and test if reachable (e.g. if we pick 32,
// then number >= 32 is unreachable), this will take O(n^2 lg n), since we do
// need O(lg (n^2)) = O(lg n) to search, and each DFS takes O(n^2)