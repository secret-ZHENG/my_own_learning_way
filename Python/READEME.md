* Basic mathmatic
1. 10^5
    10 ** 5
2. 31 ➗ 3 = 10......1     
    a = 31//3 = 10   
    b = 31%3 = 1


* Basic function
1.ord(i):return the Unicode of a string.
  ``` ord('a') ```   
2''.join():a method to concatenating elements in a sequence(such as list,tuple, e.t.c) with a specified string to generate a new string.
  ```
  words = ['Hello', 'World']
  result = '-'.join(words)
  # output : Hello-World
  ```   

* Basic code
1. trans string into upper or lower
   1.1 python convience
     ```
     s.lower()  
     s.upper()
     ```
   1.2 ASCII
     ```
      # trans lower to upper   
        s = []
        for i in str :
          if 65 <= ord(i) <= 90 :
            s.append(chr(ord(i)+32))
          else : s.append(i)
     ```   
