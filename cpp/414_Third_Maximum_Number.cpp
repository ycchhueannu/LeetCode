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
    int thirdMax(vector<int>& nums) {
        if (nums.size() == 0)
            return -2147483648;
        
        set<int> s; // std::set has order (ascending)
        for (int i = 0; i < nums.size(); ++i) {
            s.insert(nums[i]);
            if (s.size() > 3)
                s.erase(*s.begin()); // remove the smallest
        }
        
        if (s.size() == 3) return *s.begin();  // minimum element
        else               return *s.rbegin(); // maximum element
    }
};