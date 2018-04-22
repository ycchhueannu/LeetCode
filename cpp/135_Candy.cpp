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
    int candy(vector<int>& ratings) {
        // cond 1: each child at least one candy
        // cond 2: if child i ratings larger than its neighbors, then # candies
        //         must also be the most among them: (c: candy, r: ratings)
        //         c[i] > max(c[i-1], c[i+1]) if r[i] > max(r[i-1], r[i+1])
        vector<int> candy(ratings.size(),1); // cond 1 is satisified
        // this loop ensure c[i] > c[i-1] if r[i] > r[i-1]
        for (int i = 1; i < candy.size(); ++i) {
            if (ratings[i] > ratings[i-1])
                candy[i] = candy[i-1] + 1;
        }
        // this loop ensure c[i] > c[i+1] if r[i] > r[i+1], note that we need
        // to keep its original value if 'c[i+1] + 1' is smaller than c[i] 
        int sum = 0;
        for (int i = candy.size()-1; i >= 1; --i) {
            if (ratings[i-1] > ratings[i])
                candy[i-1] = max(candy[i-1], candy[i]+1);
            sum += candy[i];
        }
        sum += candy[0];
        return sum;
    }
};