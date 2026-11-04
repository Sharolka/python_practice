
# name = str(input("Enter your name: "))
# for name in range(3):
#     print(name)


#Виведи числа від 1 до 10 (включно) — кожне на новому рядку
# for i in range(1, 11):
#     print(i)

#Виведи всі числа, кратні 10, від 10 до 100 включно, в один рядок через пробіл
# for i in range(10, 101, 10):
#     print(i, end=" ")

#Запитай у користувача число n і виведи «Привіт!» рівно n разів.
# number = int(input("Enter number: "))
# for i in range(number):
#     print("Hello")

#Порахуй суму чисел від 1 до 5 за шаблоном «накопичувач». Перед запуском запиши у стовпчик, яким буде total після кожної ітерації.
# total = 0
# for number in range(1, 6):
#     total += number
#     print(total)
# print("Sum:",total)

#Порахуй добуток чисел зі списку [2, 3, 4]. Яким має бути початкове значення накопичувача?
# для множення починаємо з 1, не з 0!
# total = 1
# for number in [2,3,4]:
#     total *= number
# print(total)

#Є список colors = ["червоний", "зелений", "синій"]. Виведи кожен колір з префіксом «Колір: ».
# colors = ["червоний", "зелений", "синій"]
# for color in colors:
#     print("Color:", color)

#Виведи кожну літеру слова "python" великою (метод .upper()).
# for letter in "Python":
#     print(letter.upper())

#Виведи список ["кава", "чай", "сік"] як пронумероване меню: 1. кава, 2. чай…
# drinks = ["кава", "чай", "сік"]
# for index, drink in enumerate(drinks, start=1):
#     print(index, drink)

#Порахуй, скільки літер «а» у слові "банан"
# letter = 0
# for i in "Banana":
#     if i == "a":
#         letter +=1
# print("Total number of letters a:", letter)

#Виведи числа від 1 до 5 за допомогою while
# number = 1
# while number <= 5:
#     print(number)
#     number = number + 1

#Подвоюй число 1, поки воно менше за 100. Виведи, скільки подвоєнь знадобилось.
# number = 1
# steps = 0
# while number <= 100:
#     number *= 2
#     steps += 1
# print (number)
# print (steps)

#Виведи числа від 1 до 10, але пропусти 5 (використай continue).
# for i in range(1,11):
#     if i == 5:
#         continue
#     print (i)

#Виведи числа від 1 до 10, але зупинись, щойно дійдеш до 5 (використай break). Що буде виведено?
# for i in range(1,11):
#     if i == 5:
#         break
#     print (i)

#Є список [4, 8, 15, 16, 23, 42]. Знайди перше число, більше за 10, виведи його і зупини пошук
# numbers = [4, 8, 15, 16, 23, 42]
# for number in numbers:
#     if number > 10:
#         print(number)
#         break

#Напиши «вічний» цикл, який просить ввести слово і виводить його довжину, а на слові "стоп" завершується.
# while True:
#     word = input("Слово: ")
#     if word == "стоп":
#         break
#     print(len(word))

#Виведи всі парні числа від 1 до 20 — двома різними способами (через умову в циклі та через крок у range).
# numbers = range(1, 21)
# even = 0
# for number in numbers:
#     if number % 2 == 0:
#         print (number)
#
# for number in range(2, 21, 2):
#     print(number)

#Порахуй факторіал числа n (n! = 1·2·3·…·n). Для 5 відповідь 120
# n = 5
# result = 1
# for i in range(1, n+1):
#     result *= i
# print(result)

#Програма загадала число 42. Користувач вводить числа, поки не вгадає. Після кожної спроби пиши «більше» або «менше». У кінці — кількість спроб.
# counter = 0
# while True:
#     number = int(input("Enter a number: "))
#     counter += 1
#     if number > 42:
#         print ("Less")
#     elif number < 42:
#         print ("Greater")
#     else:
#         print (f"YES! You did {counter} attempts")
#         break

#Для числа 1234 порахуй суму його цифр (1+2+3+4 = 10). Підказка: n % 10 дає останню цифру, n // 10 відкидає її.
# n = 1234
# total = 0
# while n > 0:
#     total += n % 10
#     n = n // 10
# print(total)   # 10
# Альтернатива через рядок:
# print(sum(int(d) for d in str(1234)))
# str(1234) — перетворює число на рядок "1234".
# for d in str(1234) — перебирає кожен символ: "1", "2", "3", "4".
# int(d) — перетворює кожен символ на число.
# sum() — додає всі числа.

#Виведи трикутник із зірочок висотою 4:
# for i in range(1, 5):
#     print("*" * i)
#
# # Або через вкладені цикли:
# for i in range(1, 5):
#     for j in range(i):
#         print("*", end="")
#     print()