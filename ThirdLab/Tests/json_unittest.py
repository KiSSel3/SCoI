import unittest
import sys
sys.path.append("/home/kissel/Programming/SCoI/ThirdLab")
from Tests.data_test import my_func, my_decorator, for_dec, A, B, C
from SerilizerKiselev import JsonSerializer

class JSONTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.json = JsonSerializer()
        
    def test_int(self):
        ser_obj = self.json.dumps(12)
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(des_obj, 12)
        
    def test_list(self):
        ser_obj = self.json.dumps([1, 2, [3, 5, "sad"], "fds"])
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(des_obj, [1, 2, [3, 5, "sad"], "fds"])
        
    def test_func(self):
        ser_obj = self.json.dumps(my_func)
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(des_obj(3), my_func(3))
        
    def test_intt(self):
        ser_obj = self.json.dumps(1234)
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(des_obj, 1234)

    def test_a(self):
        ser_obj = self.json.dumps(None)
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(des_obj, None)  

    def test_b(self):
        ser_obj = self.json.dumps({1:2,2 : [2,3]})
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(des_obj, {1:2,2 : [2,3]})  

    def test_sab(self):
        ser_obj = self.json.dumps((1,2,2,3,32))
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(des_obj, (1,2,2,3,32))  

    def test_sdsab(self):
        ser_obj = self.json.dumps("sdada")
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(des_obj, "sdada")  
        
    def test_decorator(self):
        answ = my_decorator(for_dec)
        ser_obj = self.json.dumps(my_decorator)
        des_obj = self.json.loads(ser_obj)
        dec = des_obj(for_dec)
        
        self.assertEqual(answ(5), dec(5))
        
    def test_lambda(self):
        l = lambda b: b + 25
        ser_obj = self.json.dumps(l)
        des_ob = self.json.loads(ser_obj)
        
        self.assertEqual(l(2), des_ob(2))
        
    def test_static_method(self):
        ser_obj = self.json.dumps(A)
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(des_obj.ret_name(), A.ret_name())
        
    def test_decorated_static_method(self):
        obj = B()
        ser_obj = self.json.dumps(obj)
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(obj.another_method(5),des_obj.another_method(5))
        
    def test_method(self):
        obj = C()
        ser_obj = self.json.dumps(obj)
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(obj.getter(12), des_obj.getter(12))
        
    def test_init(self):
        obj = C()
        ser_obj = self.json.dumps(obj)
        des_obj = self.json.loads(ser_obj)
        
        self.assertEqual(obj.name, des_obj.name)
        
        
if __name__ == "__main__":
    unittest.main()