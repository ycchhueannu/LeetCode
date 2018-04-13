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
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        const int NUM_MAX = 100;
        const int PRICE_MAX = 1e4;
        int p[n][n]; // price
        //int Visit[n] = {0};
        #include <algorithm>
        int minCost[n];
        std::fill(&minCost[0], &minCost[n], NUM_MAX * PRICE_MAX);

        vector<vector<int>> adjList(n);
        
        // construct adjacency list
        for (int i = 0; i < flights.size(); ++i) {
            int s = flights[i][0]; // start
            int t = flights[i][1]; // end
            adjList[s].push_back(t);
            p[s][t] = flights[i][2]; // cost from s to t
        }
        
        queue<int> q_city;
        queue<int> q_stop;
        q_city.push(src); // city
        q_stop.push(0); // number of stop

        minCost[src] = 0;
        // Dijkstra's Algorithm revised (BFS-like)
        while (!q_city.empty()) {
            int city = q_city.front(); q_city.pop();
            int dist = q_stop.front(); q_stop.pop();
            if (city == dst)
                continue;
            //printf("city: %d, # stop: %d\n", city, dist);
            if (dist > K)
                break;
            
            for (int i = 0; i < adjList[city].size(); ++i) {
                int adj_c = adjList[city][i];

                // if cumulative stops reach k and hasn't reach dst, ignore, see example below
                if ((dist == K) && (adj_c != dst))
                    continue;

                if (minCost[city] + p[city][adj_c] < minCost[adj_c]) {
                    minCost[adj_c] = minCost[city] + p[city][adj_c];
                    q_city.push(adj_c);
                    q_stop.push(dist+1);
                }
            }

            
        } // end while
        
        //for (int i = 0; i < n; ++i)
        //    printf("%d ", minCost[i]);
        //printf("\n");
        
        if (minCost[dst] == NUM_MAX * PRICE_MAX)
            return -1;
        else
            return minCost[dst];
    }
    
    
    /**********************
    * w<0,1> = 1, w<0,2> = 5
    * w<1,2> = 1, w<2,3> = 1
    *             0
    *            /  \
    *           1 —— 2
    *                 \ 
    *                  3
    * src=0, dst=3, K=1
    ***********************/
};