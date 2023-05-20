import sys
sys.path.append("/home/kissel/Programming/SCoI/ThirdLab")
from Tests.data_test import my_func, my_decorator, for_dec, A, B, C
from SerilizerKiselev import JsonSerializer  

js = JsonSerializer()

def ser_test(obj):
    with open("test.json", "w") as file:
        js.dump(obj, file)
    
    with open("test.json", "r") as file:
        des_obj = js.load(file)
    
    print(des_obj)
    print("")
    
def ser_test_func(obj, arg):
    print(obj(arg))
    with open("test.json", "w") as file:
        js.dump(obj, file)
    
    print()
    
    with open("test.json", "r") as file:
        des_obj = js.load(file)
    
    print(des_obj(arg))
    print("")
    
x = 10     

ser_test(12)

ser_test(1.5)

ser_test([167, 26, 63, 874, "a"])

ser_test({1 : 10, 2 : 28, 3 : 37, "p" : 4})

ser_test((56, 77, 99, "nn", 295))

ser_test(bytes([109, 101, 108, 100, 111]))

ser_test(bytearray(b'hello world!'))

ser_test_func(my_func, 3)

#сериализация самого декоратора
with open("test.json", "w") as file:
        js.dump(my_decorator, file)

for_dec(25)    
#print(ser_obj)
print()
    
with open("test.json", "r") as file:
        des_obj = js.load(file)

df = des_obj(for_dec)
    
df(25)


#сериализация декорированной функции

df = my_decorator(for_dec)

ser_test_func(df, 25)

#сериализация анонимной функции
l = lambda b: b + 25

ser_test_func(l, 10)

with open("test.json", "w") as file:
        js.dump(A, file)
#print(cl)

with open("test.json", "r") as file:
        des_cl = js.load(file)
a = des_cl()


print(des_cl.ret_name())
print(a.my_method(5))


#Сериализация объекта
o = C()
print("Изначальные значения")
print(o.getter(5))
print("Переменная объекта: ", o.name)
print("Статический метод класса А: ", o.ret_name())
print("Статический декорированный метод класса B: ", o.another_method(10))


with open("test.json", "w") as file:
    js.dump(o, file)

with open("test.json", "r") as file:
    des_o = js.load(file)
    
print(type(des_o), des_o)

print("Десериализованные значения")
print(des_o.getter(5))
print("Переменная объекта: ", des_o.name)
print("Статический метод класса А: ", des_o.ret_name())
print("Статический декорированный метод класса B: ", des_o.another_method(10))


