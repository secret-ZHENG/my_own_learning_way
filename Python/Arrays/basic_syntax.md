# create array   
1. array module
**typed array**   
```arr = array.array('i',[1,2,3])```   
notes: 'i' : typecode  
'i' = signed int  
'b' = signed char  
'B' = unsigned char  
'f' = float  
'd' = double

2. sort   
a. list accroding to the number of arr[i]   
```idx = sorted(range(len(arr)),key = lambda i: arr[i])```
  1) from 0 to len(arr)-1
     lambda i : arr[i] : a vitural function
  2) descending order sort
     ```idx = sorted(range(len(arr)),key = lambda i: arr[i], reverse = True)```
  3) multi-conditions, such as when have same arr.
     ```
     arr = [10, 20, 10, 30]
     idx = sorted(range(len(arr)), key=lambdai: (arr[i], i))
     ➡️ [0, 2, 1, 3]
     ```
  4)use numpy
     ```
     import numpy as np  
     arr = np.array[50,30,40,10]
     idx = np.argsort(arr)
     ```
     
