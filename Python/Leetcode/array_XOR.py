148.给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。

1.Time Flexible O(n)
Space Flexible O(n)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        end = 0
        for i in range(n) :
            end ^= start + 2*i
        return end


2.Time Flexible O(1)
Space Flexible O(1)
C++
class Solution {
public:
    int sumXor(int x){
        if (x % 4 == 0) {
            return x;
        }
        if (x % 4 == 1) {
            return 1;
        }
        if (x % 4 == 2) {
            return x+1 ;
        }
        return 0 ;
    }
    
    int xorOperation(int n, int start) {
        int s = start >>1, e = n & start & 1 ;
        int ret = sumXor(s-1) ^ sumXor(s+n-1);
        return ret << 1|e;
    }
};
