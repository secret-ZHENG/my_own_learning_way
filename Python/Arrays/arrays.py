# in-place algorithm / without additional storage
''' technical requirements
1.operate directly on the input data structure
2.constant extra storage
3.no data duplication
'''
'''when to use
1.memory is scarce
2.data size is huge
3.performance-critical
4.temporary transformation- no need of original data
5.intermediate step
'''
# space complexity: O(1)
# time complexity: O(n)
def even_odd(A):
    next_even,next_odd = 0, len(A)-1
    while next_even < next_odd :
        if A[next_even] % 2 == 0 :
            next_even +=1
        else :
            A[next_even], A[next_odd] = A[next_odd],A[next_even]
            next_od
    

if __name__ == "__main__":
    A = [1,4,25,543,74,86,3,2,6,7,8]
    even_odd(A)
    print(A)
