from .serializer_functions import serialize, deserialize
import regex

class XMLSerializer:
    
    BASE_TYPES = r"str|int|float|bool|NoneType|list|dict"
    key = "key"
    val = "value"
    #именованные группы(для оращения по key и value)
    ELEMENT_P = fr"\s*(\<(?P<{key}>{BASE_TYPES})\>(?P<{val}>([^<>]*)|(?R)+)\</(?:{BASE_TYPES})\>)\s*"
    
    def dumps(self, obj):
        obj = serialize(obj)
        return self.check_value(obj)
    
    def dump(self, obj, file):
        file.write(self.dumps(obj))
        
    def check_value(self, obj):
        if (isinstance(obj, (int, float, bool, complex))):
            #print("SER INT", obj, type(obj).__name__, str(obj))
            return self._create_elem(type(obj).__name__, str(obj))
        
        if (isinstance(obj, str)):
            value = self._change_symbol(obj)
            return self._create_elem("str", value)
        
        if (isinstance(obj, list)):
            value = "".join([self.check_value(v) for v in obj])
            return self._create_elem("list", value)
        
        if (isinstance(obj, dict)):
            value = "".join([f"{self.check_value(k)}\
                                {self.check_value(v)}"\
                                for k,v in obj.items()])
            return self._create_elem("dict", value)
        
        if (not obj):
            return self._create_elem("NoneType", "None")
        
    
    def loads(self, string):
        obj = self.find_elem(string)
        return deserialize(obj)
    
    def load(self, file):
        return self.loads(file.read())
    
    def find_elem(self, string):
        string = str(string)
        string = string.strip()
        
        match = regex.fullmatch(self.ELEMENT_P, string)
        
        if (not match):
            return
        
        key = match.group("key")
        value = match.group("value")
        
        if (key == "int"):
            return int(value)
        
        if (key == "float"):
            return float(value)
        
        if (key == "str"):
            return self._change_symbol(value, True)
        
        if (key == "bool"):
            return value == "True"
        
        if (key == "complex"):
            return complex(value)
        
        if (key == "NoneType"):
            return None
        
        if (key == "list"):
            matches = regex.findall(self.ELEMENT_P, value)
            return [self.find_elem(match[0]) for match in matches]
        
        if (key == "dict"):
            matches = regex.findall(self.ELEMENT_P, value)
            return {self.find_elem(matches[i][0]):
                self.find_elem(matches[i + 1][0])\
                for i in range(0, len(matches), 2)}
        
    
    
    def _create_elem(self, name, value):
        return f"<{name}>{value}</{name}>"
    
    def _change_symbol(self, string, reverse=False):
        if (reverse):
            return string.replace("&amp;", "&").replace("&lt;", "<").\
                replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'")
        else:
            return string.replace("&", "&amp;").replace("<", "&lt;").\
                replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")
    
    