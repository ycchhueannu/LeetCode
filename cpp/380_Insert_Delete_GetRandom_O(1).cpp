// how to get Leetcode tests to run approximately 10-40% faster, since they do a lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class RandomizedSet {
public:
    #include <stdlib.h> /* srand, rand */
    #include <time.h> /* time */
    /* NULL_NUM indicate this slot is NULL (NULL is 0 which is not suitable for real number 0) */
    #define NULL_NUM 2147483648
    unordered_map<int, int> h;
    vector<long long int> v;
    int cnt_null; // count number of NULL_NUM in vector v
    
    /** Initialize your data structure here. */
    RandomizedSet() : h(), v(), cnt_null(0) {
        srand(time(NULL));
    }
    
    /** the function I defined in this problem */
    void relocate() {
        vector<long long int> vNew;
        for (int i = 0; i < v.size(); ++i) {
            if (v[i] != NULL_NUM) {
                vNew.push_back(v[i]);
                h[v[i]] = vNew.size()-1;
            }
        } // end for
        v.swap(vNew);
        cnt_null = 0;
        return;
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (h.find(val) == h.end()) {
            v.push_back(val);
            h[val] = v.size()-1;
            return true;
        }
        return false;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (h.find(val) != h.end()) {
            v[h[val]] = NULL_NUM;
            h.erase(val);
            ++cnt_null;
            if (cnt_null > v.size() / 2) { // #NULL_NUM is more than half of the vector size, needs relocate
                relocate();
            }
            return true;
        }
        return false;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        assert(v.size() != 0);
        while (true) {
            long long int num = v[rand() % v.size()];
            if (num != NULL_NUM)
                return num;            
        }
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */