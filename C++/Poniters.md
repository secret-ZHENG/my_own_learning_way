1. C++ Pointer Syntax    
   1). Declation :   
     `<variable_type> *<name>;`    
   2). declare a pointer that stors the adress of an integer   
     `int *points_to_integer;`   
      PS :'* 'is the key to declaring a pointer
     ```
     int *pointer1, non pointer1;
     int *pointer1, *pointer2;
     ```
   3). to access the actual memory location and value stores, use *   
     `call_to_function_expecting_memory_address(pointer);`
   then it evaluate to the address
   4). use '&' to get the address of a variable -- address-of operator   
   ```
   #include <iostream>
   using namespace std;
   int main()
   {
     int x;  // a normal integer
     int *p;  // a pointer to an integer
     p = &x;  //read it , "assign the address of x to p"
     cin>> x;  // Put a value in x , we could also use *p here
     cin.ignore();
     cout<< *p << "\n";  // Note the use of the * to get the value
     cin.get();
   }
   ```
   
   
     
   
