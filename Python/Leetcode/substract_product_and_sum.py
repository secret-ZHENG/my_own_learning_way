''' 1281.给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。 '''   
# 1. brute 0ms, 17.34MB
Time O(2*(n^2)), n is the digit of given number
Space O(2*n)
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # brute
        # 1. know the digit
        digit = 0
        for i in range(1,6):
            s = n // (10 ** i)
            if s == 0 :
                digit = i + 1
                break
        # 2. calculate
        origin_num = n
        add =  0
        square = 1
        for i in range(1,digit):
            add += origin_num % 10
            square *=  origin_num % 10
            origin_num = origin_num // 10 
            
        return (square - add)

''' I try to make my code more efficient. '''
#  2. 0ms,17.73MB
Time O(log n)
Space O(1)
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # improve to put the search of digit in calculation and ues "while loop"
        add, square = 0, 1
        while n != 0 :
            add += n % 10
            square *= n % 10
            n = n // 10
        return square - add
