import sys
sys.path.append("/home/kissel/Programming/SCoI/ThirdLab")
from Serializers.JSONSerializer import JsonSerializer
from Serializers.XMLSerializator import XMLSerializer

class Creator:
    
    @staticmethod
    def create_serializer(format_name : str):
        format_name = format_name.lower()
        
        if (format_name == "json"):
            return JsonSerializer()
        elif (format_name == "xml"):
            return XMLSerializer()
        else:
            raise ValueError