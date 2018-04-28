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
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> a(26, 0);
        for (char x : tasks) {
            ++a[x-'A'];
        }
        //std::sort(a.begin(), a.end(), std::greater<int>());
        priority_queue<int> q; // pq in disguise
        for (int i = 0; i < 26; ++i) {
            if (a[i] != 0)
                q.push(a[i]);
        }
        priority_queue<int> q2;
        q.push(-1); // sentinal, means end
        int elapseTime = 0;
        const int newN = n + 1; // trick is here
        int intvl = newN;
        while (!q.empty()) {
            int cur = q.top();
            //cout << "cur:" << cur << ", intvl:" << intvl << " ";
            q.pop();
            if (cur == -1) { // end
                q2.push(cur);
                if (q2.size() == 1) // only has -1, reach end
                    break;
                
                if (intvl > 0)
                    elapseTime += intvl;
                intvl = newN; // reset interval
                q.swap(q2); // push all tasks in q2 back into q
            }
            else {
                if (--cur)
                    q2.push(cur);
                ++elapseTime;
                --intvl;
                if (intvl == 0) { // push all tasks in q2 back into q
                    while (!q2.empty()) {
                        int x = q2.top();
                        q2.pop();
                        q.push(x);
                    }
                    intvl = newN; // reset intveral
                }
            }
            //cout << ", Time:" << elapseTime << "\n";
        } // end while
        
        return elapseTime;
    }
};