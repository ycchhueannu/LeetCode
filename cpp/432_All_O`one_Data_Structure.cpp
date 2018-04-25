// how to get Leetcode tests to run approximately 10-40% faster, since they do a lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class AllOne {
public:
    #define VAL_RANGE 10001 // if you assign too big, will MLE
    unordered_map<string, int> h;
    vector<unordered_set<string> > valRange;
    int minV, maxV;
    
    /** Initialize your data structure here. */
    AllOne() : h(), valRange(VAL_RANGE), minV(0), maxV(0) {
        
    }
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    void inc(string key) {
        if (h.find(key) == h.end()) {
            ++h[key];
            valRange[1].insert(key);
            minV = 1;
            maxV = max(maxV, 1);
        }
        else {
            //assert (valRange[ h[key] ].count(key) > 0);
            valRange[ h[key] ].erase(key);
            if (valRange[ h[key] ].empty() && minV == h[key])
                ++minV;
            ++h[key];
            valRange[ h[key] ].insert(key);
            maxV = max(h[key], maxV);
        }
        //printf("maxV:%d, minV:%d\n", maxV, minV);
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    void dec(string key) {
        if (h.find(key) != h.end()) {
            //assert (valRange[ h[key] ].count(key) > 0);
            valRange[ h[key] ].erase(key);
            if (valRange[ h[key] ].empty() && maxV == h[key])
                --maxV;
            if (valRange[ h[key] ].empty() && minV == h[key])
                --minV;
            --h[key];
            if (h[key] == 0)
                h.erase(key);
            else
                valRange[ h[key] ].insert(key);
            //printf("maxV:%d, minV:%d\n", maxV, minV);
        }
    }
    
    /** Returns one of the keys with maximal value. */
    string getMaxKey() {
        if (maxV == 0) {
            assert(minV == 0);
            return "";
        }
        //printf("maxV:%d, minV:%d\n", maxV, minV);
        return *valRange[maxV].begin();
    }
    
    /** Returns one of the keys with Minimal value. */
    string getMinKey() {
        if (minV == 0) {
            if (maxV == 0)
                return "";
            else {
                for (int i = 1; i <= maxV; ++i) {
                    if (!valRange[i].empty()) {
                        minV = i;
                        break;
                    }
                } // end for
            }
        }
        //printf("maxV:%d, minV:%d\n", maxV, minV);
        return *valRange[minV].begin();
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * string param_3 = obj.getMaxKey();
 * string param_4 = obj.getMinKey();
 */