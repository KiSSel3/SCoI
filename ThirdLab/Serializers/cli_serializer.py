import argparse
import sys
sys.path.append("/home/kissel/Programming/SCoI/ThirdLab")
from Serializers.Creator import Creator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Serializer of JSON, XML")
    parser.add_argument('file_from', type=str, help="file from which you load data")
    parser.add_argument('file_to', type=str, help="file to which you save serialized data")
    parser.add_argument('format_from', type=str, help="format from which you deserialize data,"+\
        "can be any of json/xml")
    parser.add_argument('format_to', type=str, help="format to which you serialize data,"+\
        "can be any of json/xml")
    
    args = parser.parse_args()
    
    from_serializer = Creator.create_serializer(args.format_from)
    to_serializer = Creator.create_serializer(args.format_to)
    
    with open(args.file_from, "w") as f_file:
        from_serializer.dump([1, 2, 3, "aboba"], f_file)
    
    with open(args.file_from) as f_file:
        obj = from_serializer.load(f_file)
    
    print(type(obj), obj)
        
    with open(args.file_to, "w") as t_file:
        to_serializer.dump(obj, t_file)