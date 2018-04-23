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
    #define LLI long long int
    int lower, upper;
    
    int divideConquer(vector<LLI>& sum, const int low, const int high) {
        if (low > high)
            return 0;
        if (low == high) { // base case
            if (lower <= sum[low] && sum[low] <= upper) // within range
                return 1;
            else
                return 0;
        }
        
        int mid = (low + high) / 2;
        int c1 = divideConquer(sum, low, mid);
        int c2 = divideConquer(sum, mid+1, high);
        int c3 = combineAndMerge(sum, low, mid, high);
        return c1+c2+c3;
    }
    
    int combineAndMerge(vector<LLI>& sum, const int low, const int mid, const int high) {
        int start = mid+1, end = mid+1; // two pointer, 'sliding window'
        int cnt = 0;
        vector<int> left_arr(&sum[low], &sum[mid]+1); // copy nums[low..mid] to left_arr
        vector<int> right_arr(&sum[mid+1], &sum[high]+1); // copy nums[mid+1..high] to right_arr

        for (int i = low; i <= mid; ++i) {
            while (start <= high && (sum[start]-sum[i]) < lower) ++start;
            while (end <= high && (sum[end]-sum[i]) <= upper) ++end;
            cnt += end - start; // within range
        } // end for
        
        /* the following is the merge part, just like merge sort */
        int i = 0, j = 0, idx = low;
        while ((i <= left_arr.size()-1) && (j <= right_arr.size()-1)) {
            if (left_arr[i] <= right_arr[j])
                sum[idx++] = left_arr[i++];
            else
                sum[idx++] = right_arr[j++];
        }
        while (i <= left_arr.size() - 1)
            sum[idx++] = left_arr[i++];
        while (j <= right_arr.size() - 1)
            sum[idx++] = right_arr[j++];
        
        return cnt;
    }
    
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        if (nums.size() == 0)
            return 0;
        this->lower = lower; // declare as 'global' variable
        this->upper = upper; // declare as 'global' variable
        // if nums = [1, 1, -3, 4] -> sum = [1, 2, -1, 3]
        vector<LLI> sum(nums.size(), 0);
        sum[0] = nums[0];
        for (int i = 1; i < nums.size(); ++i)
            sum[i] = sum[i-1] + nums[i];
        
        return divideConquer(sum, 0, sum.size()-1); // mergesort-like algorithm
    }
};