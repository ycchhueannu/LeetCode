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
    #include <algorithm> // std::random_shuffle
    vector<int> prev;
    vector<int> cur;
    Solution(vector<int> nums): prev(nums), cur(nums) {
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        // actually no need to do so, since we don't care original vector after shuffle()
        //cur = prev;
        return prev;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        random_shuffle(cur.begin(), cur.end());
        return cur;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */