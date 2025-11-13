''' 1.brute attack
Time O(n^3)   
Space O(1)  '''  
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans += 1
        return ans

''' 2.Optimize enumeration  
Time O(n(n+S))  n = len(arr), S = max(arr)=1000    
Space O(S)   
Q1:why use the last for loop ?
A1: in the for loop of j, when j add 1, we have to update arr[j] in the ARRAY[count]. 
Q2:why is 1002?
A2: we should care the district of array. When is 1001, it may show 'IndexERROR'.
'''
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        array_num = 0
        count = [0 for _ in range(1002)]
        for j in range(n):
            for k in range(j+1,n):
                if abs(arr[j]-arr[k]) <= b :
                    lj,rj = arr[j]-a, arr[j]+a
                    lk,rk = arr[k]-c, arr[k]+c
                    l = max(0,lj,lk)
                    r = min(1000,rj,rk)
                    if l <= r :
                        array_num += count[r+1] - count[l]
            for k in range(arr[j]+1,1002):
                count[k] += 1
        return array_num

