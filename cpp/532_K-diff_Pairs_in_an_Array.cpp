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
    int countDuplicate(vector<int>& nums) {
        unordered_set<int> s, dup; // if element already in 's', insert into 'dup'
        for (auto& x : nums) {
            if (!s.count(x))
                s.insert(x);
            else
                dup.insert(x);
        }
        return dup.size();
    }
    
    int findPairs(vector<int>& nums, int k) {
        if (nums.size() < 2 || k < 0)
            return 0;
        else if (k == 0) {
            return countDuplicate(nums); // O(n)
        }
        // k > 0, O(n)
        int cnt = 0;
        unordered_map<int, list<int> > h;
        for (const auto x : nums) {
            if (h.find(x) == h.end()) {
                h[x] = {x-k, x+k};
            }
            if (h.find(x-k) != h.end() && !h[x-k].empty() && h[x-k].back() == x) {
                ++cnt;
                h[x-k].pop_back();
                h[x].pop_front();
            }
            if (h.find(x+k) != h.end() && !h[x+k].empty() && h[x+k].front() == x) {
                ++cnt;
                h[x+k].pop_front();
                h[x].pop_back();
            }
        }
        return cnt;
    }
};
// O(n lg n)
/*
        if (nums.size() < 2 || k < 0)
            return 0;
        vector<int> uniqueNum;
        unordered_set<int> setNum;
        unordered_set<int> dup;
        for (auto& n : nums) {
            if (setNum.count(n) == 0) { // not found
                uniqueNum.push_back(n);
                setNum.insert(n);
            }
            else {
                dup.insert(n);
            }
        } // end for
        if (k == 0)
            return dup.size();
        
        std::sort(uniqueNum.begin(), uniqueNum.end());
        int s = 0, t = 1; // start and end
        int ans = 0;
        while (t < uniqueNum.size()) {
            if (uniqueNum[t] - uniqueNum[s] == k) {
                ++ans;
                ++s;
                ++t;
            }
            else if (uniqueNum[t] - uniqueNum[s] > k) {
                ++s;
                if (s == t)
                    ++t;
            }
            else { // uniqueNum[t] - uniqueNum[s] < k
                ++t;
            }
        } // end while
        return ans;
*/