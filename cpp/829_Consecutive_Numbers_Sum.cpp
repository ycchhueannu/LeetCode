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
    int consecutiveNumbersSum(int N) {
        int ans = 0;
        int ub = int(sqrt(2*N));
        for (int i = 1; i <= ub; ++i) {
            long long int s = i*(i-1)/2; 
            if ((N-s) % i == 0)
                ++ans;
        }
        return ans;
    }
};
// N = x + (x+1) + (x+2) + ... + (x+(n-1))
// Thus, N = nx + n*(n-1)/2, and both terms should > 0
// That is, N > n*(n-1)/2 -> 2N + 0.25 > (n-0.5)^2 => n < sqrt(2N)
// N = nx + n*(n-1)/2 -> x = [N - n(n-1)/2] / n, where x is integer