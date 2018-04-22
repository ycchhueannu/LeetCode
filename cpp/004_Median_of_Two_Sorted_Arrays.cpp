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
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        #define INT_MIN -2147483648
        #define INT_MAX 2147483647
        if (nums1.size() > nums2.size())
            return findMedianSortedArrays(nums2, nums1); // swap nums1 and nums2
        int m = nums1.size();
        int n = nums2.size();
        int aveOfmn = (m + n) / 2; // average of m and n
        int mid_i = (m-1) / 2;
        int mid_j;
        while (true) {
            mid_j = aveOfmn - mid_i;
            //assert(mid_j >= 0);
            int p = (mid_i - 1) < 0 ? INT_MIN : nums1[mid_i-1];
            int q = (mid_i >= m)    ? INT_MAX : nums1[mid_i];
            int r = (mid_j - 1) < 0 ? INT_MIN : nums2[mid_j-1];
            int s = (mid_j >= n)    ? INT_MAX : nums2[mid_j];
            //printf("%d %d %d %d\n", p, q, r, s);
            if (p <= s && r <= q) {
                if ((m + n) % 2 == 0)
                    return ( max(p, r) + min(q, s) ) / 2.0;
                else
                    return min(q, s);
            }
            else if (p > s) { // mid_i backward, mid_j forward
                --mid_i;
            }
            else { // (r > q), mid_i forward, mid_j backward
                ++mid_i;
            }
        } // end while
    }

};


/*
                                (split)        idx 0 1 2 3   4 5 6 7 8 9
    array A (size m=10): A[0..i-1] / A[i..m-1]     _ _ _ p / q _ _ _ _ _ 
                                               =>  
    array B (size n=12): B[0..j-1] / B[j..n-1]     _ _ _ _ _ _ r / s _ _ _ _ _  
    
    
    since we want left part length A & B == right part length A & B, i.e.
    i + j == (m + n) - (i + j) => i + j = floor( (m+n)/2 ) (ignore floor
    for now)
    So given i, "j = (m+n)/2 - i". since i ranges from 0 ~ m (if i = 0, then
    entire A is on the right part; if i = m, entire A is on the left part),
    we need to ensure j always larger than or equal to 0.
    That is, j = (m+n)/2 - m = (n-m) / 2 >= 0, thus n >= m (Therefore, if
    n > m, then we just swap two arrays and then solve it.)
    
    We can deal with when to stop the iteration now: Given p, q, r, s defined
    as above, desire case is max(p, r) <= min(q, s), that is, maximum element
    in left part array is smaller than or equal to the the minimum of the right.
    Or equivalently, condition "p <= s and r <= q" (A, B are already sorted)
    Once this condition holds, we can return the median of two sorted array
    
    There may be two conditions if the above condition does not hold:
    0. p > s, then we need to decrease i (thus j is incremented by 1)
    1. r > q, then we need to increase i (thus j is decremented by 1)
    (think about why p > s and q > r can't happen. hint: A, B are sorted array)

*/