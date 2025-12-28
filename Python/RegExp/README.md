1. What is it?
   To search, replace, veritify and gain.
2. Syntax  
   `^[a-zA-Z0-9_-]{3,15}$`  
   '^' and '$' : begin and end 
   [] : character set
   {3,15} : character set appear 3~15 times
3. basic   
  1) Times   
     '*' : match 0 or many times
     '+' : match 1 or many times
     '?' : match 0 or 1
     '{n}' : match n times
     '{n,}' : match at least n times
     '{n,m}': match more than n times, less than m times   
    2) character match   
     '\d]\' : match random number character   
     '\w' : match random char character   
    3) Character    
     '[]' : match what in '[]'
     '[^]' : match what out of '[]'
     4) boundary
     '^' and '$' : begin and end
     '\b': word  
     '\B' : nonword
    5) group and capture       
    '()' and '(?:)' : group & capture and group & no capture
  6) special
     '\' : match special character itself
     '.' : match random character (exp change line)
     '|' : choice of many models
     

   


   
