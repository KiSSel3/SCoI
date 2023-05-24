import unittest
import sys
sys.path.append("/home/kissel/Programming/SCoI/ThirdLab")
from Tests.data_test import my_func, my_decorator, for_dec, A, B, C
from SerilizerKiselev import XMLSerializer

class XMLTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.xml = XMLSerializer()
        
    def test_int(self):
        ser_obj = self.xml.dumps(12)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, 12)
        
    def test_list(self):
        ser_obj = self.xml.dumps([1, 2, [3, 5, "sad"], "fds"])
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, [1, 2, [3, 5, "sad"], "fds"])
        
    def test_func(self):
        ser_obj = self.xml.dumps(my_func)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj(3), my_func(3))
        
    def test_decorator(self):
        answ = my_decorator(for_dec)
        ser_obj = self.xml.dumps(my_decorator)
        des_obj = self.xml.loads(ser_obj)
        dec = des_obj(for_dec)
        
        self.assertEqual(answ(5), dec(5))
        
    def test_lambda(self):
        l = lambda b: b + 25
        ser_obj = self.xml.dumps(l)
        des_ob = self.xml.loads(ser_obj)
        
        self.assertEqual(l(2), des_ob(2))
        
    def test_static_method(self):
        ser_obj = self.xml.dumps(A)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj.ret_name(), A.ret_name())
        
    def test_decorated_static_method(self):
        obj = B()
        ser_obj = self.xml.dumps(obj)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(obj.another_method(5),des_obj.another_method(5))

    def test_intt(self):
        ser_obj = self.xml.dumps(1234)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, 1234)

    def test_bool(self):
        ser_obj = self.xml.dumps(True)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, True)    

    def test_boolF(self):
        ser_obj = self.xml.dumps(False)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, False)  


    def test_a(self):
        ser_obj = self.xml.dumps(None)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, None)  

    def test_b(self):
        ser_obj = self.xml.dumps({1:2,2 : [2,3]})
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, {1:2,2 : [2,3]})  

    def test_sab(self):
        ser_obj = self.xml.dumps((1,2,2,3,32))
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, (1,2,2,3,32))  

    def test_sdsab(self):
        ser_obj = self.xml.dumps("sdada")
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, "sdada")  
    
    def test_method(self):
        obj = C()
        ser_obj = self.xml.dumps(obj)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(obj.getter(12), des_obj.getter(12))
        
    def test_init(self):
        obj = C()
        ser_obj = self.xml.dumps(obj)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(obj.name, des_obj.name)
        
        
if __name__ == "__main__":
    unittest.main()