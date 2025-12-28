# What is it?   
   To search, replace, veritify and gain.   
# Syntax  
   `^[a-zA-Z0-9_-]{3,15}$`  
   '^' and '$' : begin and end   
   [] : character set   
   {3,15} : character set appear 3~15 times   
# basic   
## Times     
     '*' : match 0 or many times   
     '+' : match 1 or many times   
     '?' : match 0 or 1   
     '{n}' : match n times   
     '{n,}' : match at least n times   
     '{n,m}': match more than n times, less than m times    
## character match   
     '\d' : match random number character   
     '\w' : match random char character(= [A-Za-z0-9])      
## Character    
     '[]' : match what in '[]'
     '[^]' : match what out of '[]'   
## boundary
     '^' and '$' : begin and end
     '\b': word boundary   
     '\B' : nonword boundary   
## group and capture          
    '()' and '(?:)' : group & capture and group & no capture   
## special   
     '\' : match special character itself   
     '.' : match random character (exp change line--\n & \r)   
     '|' : choice of many models   
     '\s\S': match all whitespace (include liner), all non whitespace   
     
     

   


   
