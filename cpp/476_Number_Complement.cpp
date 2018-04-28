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
    int findComplement(int num) {
        unsigned int mask = ~0;
        while (num & mask) // how many bits do num need (no leading zero)
            mask = mask << 1;
        return ~mask & ~num;
    }
};
/*
original:
mask         = 11111111
num          = 00000101

after while loop:
num          = 00000101
mask         = 11111000

~mask & ~num = 00000010
*/