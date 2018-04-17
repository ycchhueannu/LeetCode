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
    bool checkPossibility(vector<int>& nums) {
        int isModify = 0;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < nums[i-1]) {
                if (isModify)
                    return false;
                if (i < 2 || nums[i] >= nums[i-2]) {
                    nums[i-1] = nums[i];
                }
                else
                    nums[i] = nums[i-1];
                isModify = 1;
            } // end if
        } // end for
        
        return true;
    }
};
// invariant: a0 <= a1 <= a2 <= ... <= an
// when a[n] < a[n-1], under this condition, there may be two cases: (... a[n-2], a[n-1], a[n], ...)
// 1. a[n] >= a[n-2], or 2. a[n] < a[n-2]
// condition 1 (a[n-2] <= a[n] < a[n-1]) means we should scale a[n-1] down, e.g. [.. 3, 7, 4 ..] -> [.. 3, 4, 4 ..]
// condition 2 (a[n] < a[n-2] <= a[n-1]) means we should scale a[n] up, e.g. [.. 7, 8, 5 ..] -> [.. 7, 8, 8 ..]