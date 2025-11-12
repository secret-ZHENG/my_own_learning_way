1.brute attack


# 2.Optimize enumeration
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        array_num = 0
        count = [0 for _ in range(1010)]
        for j in range(n):
            for k in range(j+1,n):
                if abs(arr[j]-arr[k]) <= b :
                    lj,rj = arr[j]-a, arr[j]+a
                    lk,rk = arr[k]-c, arr[k]+c
                    l = max(0,lj,lk)
                    r = min(1000,rj,rk)
                    if l <= r :
                        array_num += count[r+1] - count[l]
            for k in range(arr[j]+1,1010):
                count[k] += 1
        return array_num

