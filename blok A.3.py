num1 = int(input("Введите целое число: "))
num2 = 0
while num1 > 0:
    arr = num1 % 10
    num1 = num1 // 10
    num2 = num2 * 10
    num2 = num2 + arr  
print('"Обратное" ему число:', num2)