// how to get Leetcode tests to run approximately 10-40% faster, since they do a lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class MinStack {
public:
    /** initialize your data structure here. */
    std::stack<int> stk;
    std::stack<int> minRec; // record minimum
    
    MinStack() {
        // do nothing
    }
    
    void push(int x) {
        stk.push(x);
        int elt;
        //int elt = minRec.empty() ? x : min(minRec.top(), x);
        if (!minRec.empty())
            elt = min(minRec.top(), x);
        else
            elt = x;
        minRec.push(elt);
    }
    
    void pop() {
        stk.pop();
        minRec.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minRec.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */