countNumbers = input("Введите количество чисел: ")
while not countNumbers.isdigit():
    countNumbers = input("Ошибка!\nВведите количество чисел: ")

numbers = range(int(countNumbers))

print("Список чисел:")
for item in numbers:
    print(item, end=" ")


evenNumbers = numbers[2::2]

if evenNumbers:
    print("\nЧётные числа:")
    for item in evenNumbers:
        print(item, end=" ")
else:
    print("Чётные числа отсутствуют!")

print("\n")