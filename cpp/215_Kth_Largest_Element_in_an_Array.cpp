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
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<long long int> pq; // long long int avoid edge cases like -2147483648
        for (long long int x : nums) {
            pq.push(-x);
            if (pq.size() > k)
                pq.pop();
        }
        return -pq.top();
    }
};