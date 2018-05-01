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
    int maxChunksToSorted(vector<int>& arr) {
        int ans = 0;
        int max = arr[0]; // max index
        for (int i = 0; i < arr.size(); ++i) {
            if (arr[i] > max) {
                max = arr[i];
            }
            else if (i == max) {
                ++ans;
                max = arr[i+1];
            }
        }
        return ans;
    }
};