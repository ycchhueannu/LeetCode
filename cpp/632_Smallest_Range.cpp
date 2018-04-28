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
    #include <functional> // std::greater
    #include <utility> // std::pair
    #define PAIR pair<int,int>
    
    vector<int> smallestRange(vector<vector<int>>& nums) {
        vector<int> nextRec(nums.size(), 0); // record next index
        priority_queue<PAIR, vector<PAIR>, std::greater<PAIR> > minPQ;
        int maxElt = -2147483648; // max element in minPQ;
        for (int i = 0; i < nums.size(); ++i) {
            int nextIdx = nextRec[i];
            if (nextIdx < nums[i].size()) {
                minPQ.push( {nums[i][nextIdx], i} );
                maxElt = max(maxElt, nums[i][nextIdx]);
                ++nextRec[i];
            }
        }
        
        int minDist = 2147483647; // smallest range
        int start = -1;
        while (minPQ.size() == nums.size()) {
            PAIR p = minPQ.top();
            minPQ.pop();
            int newDist = maxElt - p.first;
            if (newDist < minDist) {
                start = p.first;
                minDist = newDist;
            }
            int nextIdx = nextRec[p.second];
            if (nextIdx < nums[p.second].size()) {
                minPQ.push( {nums[p.second][nextIdx], p.second} );
                ++nextRec[p.second];
                maxElt = max(maxElt, nums[p.second][nextIdx]);
            }        
        } // end while
        return {start, start + minDist};
    }
};

// or you can use two pointer (like minimum sliding window):
// fist construct pairs (value number, index in vector), sort
// by value, and then scan from left to right
// e.g. [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
//  val: [0, 4, 5, 9, 10, ...]
//  idx: [1, 0, 2, 1,  0, ...]