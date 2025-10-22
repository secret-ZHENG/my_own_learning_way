1512.给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。

1.暴力拆解
Time Flexiable : O(n^2)
Space Flexiable :O(1)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = 0
        for i in range(len(nums)) :
            for j in range(i+1, len(nums)):
                if nums[i] == nums [j] and i < j:
                    counts += 1
        return counts

2.0ms
Time Flexiable : O(n)
Space Flexiable :O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = [0 for _ in range(101)]
        result = 0
        for num in muns:
            result += counter[num]   
            counter[num] += 1   
        ‘’‘优化下面循环
        for num in nums :
            counter[num] += 1
        for count in counter :
            result += (count) * (count -1) // 2
            ’‘’
        return result
