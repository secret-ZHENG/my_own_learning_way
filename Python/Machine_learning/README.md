# Numpy
1."f_wb = np.zeros(m)" :product a one dimension array(length = m)  
"np.shape(array)" : attain the dimension : eg-array([[1,2,3],[2,3,4]]) 's shape is (2,3)  
   
2."import math/copy"   
&  math:provide math function and parameters like pi : can influen the origin     
&  copy: provide "copy.copy()" and "copy.deepcopy"     
   
3."math.ceil" : return the minimum integer which >= the given count  
"math.floor" : return the maxmum integer which <= the given count   
   
4."{i:4}" : 4 number    
"{j:0.2e-03}" : exponential appearence : = 0.0002  
"8.4f" : 8 width and 4 number after point, f is fixed-point  

5. ```
   try :
      # error
   except Exception as e:
   ```
   "except" : attain all abnormality include system exit, but cannot get abnormality object
   "except ValueError" : only get special abnormality, such as number error
   "except Exception as e" : get common abnormality except system exit, keyboard pause, etc.
   
6. "np.dot(a,b)" : a0*b0 + a1*b1 + ... + an*bn

7."np.set_printoptions(precision=2)" : set print type format , 2number after point  

# matplotlib  
1. plt.plot: suitable for line charts   
   plt.scatter: No lines, only dots, with individual color and size control for each dot.
2. plt.scatter(x, y, s=None, c=None, marker='o', alpha=None, ...)
   x,y : coordinates   
   c: the color of point
   marker : the shape of the point (like 'o' circle, '^' triangle  
   alpha: transparency (0 to 1)
   
   
   




   




