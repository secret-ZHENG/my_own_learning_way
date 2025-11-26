This is my test and learn note about array! I record what I read, look, watch and try.  
# forcus on Jwasham's asked ability   
Implement a vector (mutable array with automatic resizing):
## 1. Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.➡️C++
* comprehension  : python do not have explicit pointer
### First way: using *bytearray* and *memoryview*

## 2. New raw data array with allocated memory

## 3.comprehension of code
* size()-number of items   
* capacity()-number of items it can hold   
* is_empty()-a method name convention to check whether a data structure contains no elements
    used for: data structures like list, stacks, queues, trees, etc.
    benefit: better readability, encapsulation, consistent interface
* at(index) - returns the item at a given index, blows up if index out of bounds   
  ```
  # safe element access with default
  def safe_at(collection, index. default = None):
    try:
      return collection[index]
    except (IndexError, KeyError):
      return default
  # usage
  my_list = [1, 2, 3]
  print(safe_at(my_list, 5, 'Not found'))
  ```
* 

