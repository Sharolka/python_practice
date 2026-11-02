#Запитай у користувача число і виведи «Парне» або «Непарне»
number = int(input("Enter your number: "))
if number %2 == 0:
    print("Even")
else:
    print("Odd")

# Є три змінні a, b, c. Виведи найбільше число (без використання max())
a = 1
b = 5
c = 10
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)

# Запитай два числа та операцію (+, -, *, /). Виведи результат. Якщо ділення на нуль — виведи «Ділити на нуль не можна». Якщо операція невідома — «Невідома операція».
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
operation = input("Enter operation: ")
if operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
elif operation == "*":
    print(number_1 * number_2)
elif operation == "/":
        if number_2 == 0:
            print("Division by zero impossible")
        else:
            print(number_1 / number_2)
else:
    print("Unknown operation")

#Рік високосний, якщо він ділиться на 4, але не ділиться на 100 — або ділиться на 400. Запитай рік і виведи відповідь.
year = int(input("Enter your year: "))
if year % 4 == 0 and year % 100 != 0:
    print("Цей рік високосний")
else:
    print("Цей рік не високосний")
