import ctypes  
ll = ctypes.cdll.LoadLibrary   
lib = ll("./libsample.so")    
print lib.foo(1, 3)  

