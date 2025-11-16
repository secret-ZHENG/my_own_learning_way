'''
1. brute_answer 7ms , 17.53MB   
Time O(n)
Space O(n)
'''
class Solution:
    def addDigits(self, num: int) -> int:
        # find each num
        n = str(num)
        # add
        while len(n) > 1 :
            n_sum = 0
            for e in n :
                n_sum += int(e)
            n = str(n_sum)
        return int(n)

'''
2. math 0 ms, 17.67MB
Time O(1)
Space O(1)
'''
class Solution:
    def addDigits(self, num: int) -> int:
        return(((num-1)%9+1) if num else 0)
