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
        if (arr.size() < 1)
            return -1;
        long long int sum1 = 0, sum2 = 0;
        int ans = 0;
        vector<int> tmp = arr;
        sort(tmp.begin(), tmp.end());
        for (int i = 0; i < arr.size(); ++i) {
            sum1 += arr[i];
            sum2 += tmp[i];
            if (sum1 == sum2)
                ++ans;
        }
        return ans;
    }
};
// naive method: use multiset, for each iteration check if two sets are equal
// (first is unsorted, the other is sorted) -> O(n^2)
/*
        if (arr.size() < 1)
            return -1;
        int n = arr.size();
        vector<int> rightMin(n); // rightMin[i] means min value in arr[i:]
        rightMin[n-1] = arr[n-1];
        for(int i = n-2; i >= 0; --i)
            rightMin[i] = min(arr[i], rightMin[i+1]);
        
        int ans = 1, curMax = arr[0];
        for (int i = 1; i < n; ++i) {
            if (rightMin[i] < curMax)
                curMax = max(curMax, arr[i]);
            else {
                ++ans;
                curMax = arr[i];
            }
        }
        return ans;
*/