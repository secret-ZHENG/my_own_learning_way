class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1)
        #1. return n if n % 2 ==0 else n*2
        '''2.
        return (n % 2 + 1) * n
        '''
        '''3.
        if n % 2 == 0 :
            return n
        else :
            return n * 2
        '''
        '''4.
        return (n % 2 + 1) * n
        '''
