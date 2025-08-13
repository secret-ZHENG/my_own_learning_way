# basic syntax
& 'AND"   
| 'OR'   
^ 'XOR' : if same, print 0; if different, print 1   
~ 'NOT':0 transfer to 1, 1 transfer to 0   
<< '*(2^n)'   
">> '/(2^n)'  "  
#  print binary of an integer
1. function bin
```python
bin(x)      # '0b010'
bin(x)[2:]  # '010'
```
3. use format string
``` python
f"{x:b}"        # '010'   
format(x,'b')   # '010'
f"{x:08b}"      # '00000010'  'display bite's width is 8'  
```
