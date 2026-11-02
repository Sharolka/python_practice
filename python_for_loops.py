# Create the fruits list
fruits = ["apple", "banana", "cherry"]
# Loop through fruits, break at "banana"
for x in fruits:
    print(x)
    if x == "banana":
      break

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total_odd = 0
# total_even = 0
# for number in numbers:
#     if number % 2 == 0:
#         total_odd += number
#         print("Even:", number)
#     else:
#         total_even += number
#         print("Odd:", number)
#
# print(total_odd)
# print(total_even)

# for number in range(2, 12, 2):
#     print(number)

# for number in range(1,11):
#     if number % 2 != 0:
#         print(f"Odd numbers: {number}")
#     else:
#         print(f"Even numbers: {number}")

# even_sum = 0
# odd_sum = 0
# for number in range (1,11):
#     if number % 2 == 0:
#         even_sum += number
#     else:
#         odd_sum += number
#
# print(f"Even numbers: {even_sum}")
# print(F"Odd numbers {odd_sum}")

# even_quantity = 0
# odd_quantity = 0
# for number in range(1,21):
#     if number % 2 == 0:
#         even_quantity += 1
#     else:
#        odd_quantity += 1
#
# print(f"Even quantity is {even_quantity}")
# print(f"Odd quantity is {odd_quantity}")


even_sum = 0
odd_quantity = 0
for number in range(1,11):
    if number % 2 == 0:
        even_sum += number
    elif number% 2 != 0:
        odd_quantity += 1

print(f"Even sum is {even_sum}")
print(f"Odd quantity is {odd_quantity}")