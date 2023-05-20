import math

x = 102   
def my_func(a):
    return math.sin(a - x)

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        res = func(*args, **kwargs)
        print("Function ended")
        return res
        
    return wrapper

#@my_decorator
def for_dec(a):
    print("Hello World!!!!!!!!", a)
    
X = 12
class A:
    name = "Arsenii"
    
    
    @staticmethod
    def ret_name():
        return A.name
    
    def my_method(self, x):
        return x + 532

class B:
    @staticmethod
    @my_decorator
    def another_method(k):
        print("Hello")
        return math.sin(k / X)

class C(A, B):
    def __init__(self):   
        self.name = "my name"
        
    def getter(self, k):
        return k