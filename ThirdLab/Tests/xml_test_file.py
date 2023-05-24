import sys
sys.path.append("/home/kissel/Programming/SCoI/ThirdLab")
from Tests.data_test import my_func, my_decorator, for_dec, A, B, C
from SerilizerKiselev import XMLSerializer

serializer_xml = XMLSerializer()

def ser_test(obj):
    with open("test.xml", "w") as file:
        serializer_xml.dump(obj, file)
    
    with open("test.xml", "r") as file:
        des_obj = serializer_xml.load(file)
    
    print(des_obj)
    print("")
    
def ser_test_func(obj, arg):
    print(obj(arg))
    with open("test.xml", "w") as file:
        serializer_xml.dump(obj, file)
    
    #print(ser_obj)
    print()
    
    with open("test.xml", "r") as file:
        des_obj = serializer_xml.load(file)
    
    print(des_obj(arg))
    print("")
    
x = 102    
    

ser_test(123)

ser_test(1.325)

ser_test([13, 21, 34, 24, "A"])

ser_test({12 : 1, 22 : 2, 33 : 3, "C" : 4})

ser_test((5, 7, 9, "B", 25, True, None))

ser_test(bytes([101, 108, 109, 111, 102]))

ser_test(bytearray(b'hello world!'))

ser_test_func(my_func, 5)

#сериализация самого декоратора
with open("test.xml", "w") as file:
        serializer_xml.dump(my_decorator, file)

for_dec(330)    
#print(ser_obj)
print()
    
with open("test.xml", "r") as file:
        des_obj = serializer_xml.load(file)

df = des_obj(for_dec)
    
df(253)
print("")

#сериализация декорированной функции

df = my_decorator(for_dec)

ser_test_func(df, 25)

#сериализация анонимной функции
l = lambda b: b + 25

ser_test_func(l, 10)

with open("test.xml", "w") as file:
        serializer_xml.dump(A, file)
#print(cl)

with open("test.xml", "r") as file:
        des_cl = serializer_xml.load(file)
a = des_cl()


print(des_cl.ret_name())
print(a.my_method(5))

print("")

#Сериализация объекта
o = C()
print("Изначальные значения")
print(o.getter(5))
print("Переменная объекта: ", o.name)
print("Статический метод класса А: ", o.ret_name())
print("Статический декорированный метод класса B: ", o.another_method(120))


with open("test.xml", "w") as file:
    serializer_xml.dump(o, file)

with open("test.xml", "r") as file:
    des_o = serializer_xml.load(file)

print("Десериализованные значения")
print(des_o.getter(5))
print("Переменная объекта: ", des_o.name)
print("Статический метод класса А: ", des_o.ret_name())
print("Статический декорированный метод класса B: ", des_o.another_method(120))


