def function(firstNumber, secondNumber, operation):
    if operation == "add":
        return float(firstNumber) + float(secondNumber)
    
    if operation == "sub":
        return float(firstNumber) - float(secondNumber)
    
    if operation == "mult":
        return float(firstNumber) * float(secondNumber)
    
    if operation == "div":
        return float(firstNumber) / float(secondNumber)


def isNumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


firstNumber = input("Введите первое число: ")
while  not isNumber(firstNumber):
    firstNumber = input("Ошибка! Введённое значение не является числлом.\nВведите первое число: ")   

secondNumber = input("Введите второе число:")
while  not isNumber(secondNumber):
    secondNumber = input("Ошибка! Введённое значение не является числлом.\nВведите второе число: ") 

operation = input("Выберите действие над числами(add, sub, mult, div): ")
while operation != "add" and operation != "sub" and operation != "mult" and operation != "div":
     operation = input("Ошибка! Такого действия нет.\nВыберите действие над числами(add, sub, mult, div): ")

print(f"Полученное значение: {function(firstNumber,secondNumber,operation)}")     
