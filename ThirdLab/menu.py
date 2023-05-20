from SerilizerKiselev import JsonSerializer
from SerilizerKiselev import XMLSerializer

while True:
    print('Enter 1 to get from json')
    print('Enter 2 to get from xml')
    print('Enter 3 to convert json to xml')
    print('Enter 4 to convert xml to json')
    print('Enter 5 to exit')

    js = JsonSerializer()
    xs = XMLSerializer()
    choice = input("Choose one option: ")

    if choice == '1':
        filename = input('Enter filename: ')
        with open(filename, "r") as file:
            print(js.load(file))
    elif choice == '2':
        filename = input("Enter filename: ")
        with open(filename, "r") as file:
            print(xs.load(file))
    elif choice == '3':
        json_filename = input("Enter json filename: ")
        with open(json_filename , "r") as file1:
            xml_filename = input('Enter xml filename: ')
            with open(xml_filename, "w") as file2:
                obj = js.load(file1)
                xs.dump(obj, file2)
    elif choice == '4':
         xml_filename = input("Enter xml filename: ")
         with open(xml_filename , "r") as file1:
            json_filename = input('Enter json filename: ')
            with open(json_filename, "w") as file2:        
                obj = xs.load(file1)
                js.dump(obj, file2)
    elif choice == '5':
        break
    else:
        print('Incorrect input. Try again.')