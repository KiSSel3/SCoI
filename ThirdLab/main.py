
from SerilizerKiselev import JsonSerializer
from SerilizerKiselev import XMLSerializer

ser_json = JsonSerializer()

class A:
    x = 135
    
    def __init__(self) -> None:
        self.a = 122
        self.b = 103
    
    def my_meth(self):
        return self.a * self.b
    
    
class B:
    def __str__(self):
        return "swa"
    
    def __repr__(self):
        return "swa"
    
    
class C(A, B):
    pass


obj = C()
obj_s = ser_json.dumps(obj)
obj_d = ser_json.loads(obj_s)


print(obj_d.my_meth()) 
print(obj_d.x)
print(obj_d)



ser_xml = XMLSerializer()

class D:
    y = 145
    
    def __init__(self) -> None:
        self.a = 123
        self.b = 130
    
    def my_meth(self):
        return self.a + self.b
    
    
class E:
    def __str__(self):
        return "Class e"
    
    def __repr__(self):
        return "Classs E"
    
    
class F(D, E):
    pass


obj = F()
obj_s = ser_xml.dumps(obj)
obj_d = ser_xml.loads(obj_s)


print(obj_d.my_meth()) 
print(obj_d.y)
print(obj_d)






