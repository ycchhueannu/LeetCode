// how to get Leetcode tests to run approximately 10-40% faster, since they do a lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class RandomizedCollection {
public:
    #include <stdlib.h> /* srand, rand */
    #include <time.h> /* time */
    /* NULL_NUM indicate this slot is NULL (NULL is 0 which is not suitable for real number 0) */
    #define NULL_NUM 2147483648
    unordered_map<long long int, int> freq; // store NULL_NUM as well
    unordered_map<int, queue<int>> pos;
    vector<long long int> v;
    
    /** Initialize your data structure here. */
    RandomizedCollection() {
        freq.clear();
        pos.clear();
        v.clear();
        srand(time(NULL));
    }
    
    /** the function I defined in this problem */
    void relocate() {
        vector<long long int> vNew;
        for (int i = 0; i < v.size(); ++i) {
            if (v[i] != NULL_NUM) {
                vNew.push_back(v[i]);
                pos[v[i]].pop();
                pos[v[i]].push(vNew.size()-1);
            }
            
        } // end for;
        v.swap(vNew);
        freq[NULL_NUM] = 0; // reset
        return;
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        ++freq[val];
        v.push_back(val);
        pos[val].push(v.size()-1);
        if (freq[val] == 1)
            return true;
        return false;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        if (freq.find(val) != freq.end()) {
            --freq[val];
            int del_idx = pos[val].front();
            pos[val].pop();
            v[del_idx] = NULL_NUM;
            ++freq[NULL_NUM];
            if (freq[NULL_NUM] > v.size() / 2) { // #NULL_NUM is more than half of the vector size, needs relocate
                relocate();
                //cout << "after relocate, v.size ="<< v.size() << "\n";
            }
            if (freq[val] == 0) {
                freq.erase(val);
            }
            return true;
        }
        return false;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        while (1) {
            long long int rand_num = rand() % v.size();
            if (v[rand_num] != NULL_NUM)
                return v[rand_num];
        }
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */