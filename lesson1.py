# print("hello world, I'm learning python")
#
# #varibale
# age = 25
# print(age)
#
# age1 = 30
# print(age1)
#
# price = 100
# print(price)
#
# price2 = 200
# print(price2)
#
# #basic arithmetic operation
# a = 10
# b = 15
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)
#
# c = 10
# d = 3
# print(c + d)
# print(c - d)
# print(c * d)
# print(c / d)
#
# #input
# name = input("Please enter your name: ")
# print("hello", name)
#
# #calclator
# x =input("Please enter first number: ")
# y = input("Please enter second number: ")
#
# x  = int(x)
# y  = int(y)
#
# result = x + y
# result1 = x * y
# print(result , result1)


##sum
# print(int("5") + int("6"))

##comparisons
# print(5 > 3)  #greater
# print(5 < 3)  #less
## single = is assigns  double == is compares
# print(5 == 5) #equal
# print(5 != 5) #not equal


##if
# age = int(input("Enter your age: "))
#
# if age >= 18:
#     print("You are an adult")
#
# print("program finished")

##if else
# age = input("What is your age?")
#
# if int(age) >= 18:
#     print("You are an adult.")
# else:
#     print("You are under 18.")

# number = int(input("Enter a number: "))
#
# if number > 100:
#     print("large number")
# else:
#     print("small number")

# #elif
# age = int(input("What is your age?"))
#
# if age < 18:
#     print("child")
# elif age < 60:
#     print("adult")
# else:
#     print("senior")

# score = int(input("Enter your score: "))
#
# if score >= 90:
#     print("A")
# elif score >= 70:
#     print("B")
# elif score >= 50:
#     print("C")
# else:
#     print("Fail")

# #logical operation and/or
# age = int(input("Enter your age: "))
# income = int(input("Enter your InCOME: "))
#
# if age >= 18 and income >= 1000:
#     print("approved")
# else:
#     print("not approved")

# temp = int(input("Enter your temp: "))
#
# if temp > 30:
#     print("Hot")
# elif temp >= 15 and temp <= 30:
#     print("Normal")
# elif temp < 15:
#     print("Cold")

# #Loop

# #while
# count = 1
# while count <= 5:
#     print(count)
#     count += 1 #if you forget loop never ends

# #for
# for i in range(1, 6):
#     print(i)

# for i  in  range(1, 10):
#     print(i)

# for i in range(1, 20):
#     if i % 2 == 0:
#        print("even:", i)
#     else:
#        print("odd:", i)

# while True:
# number = int(input("enter your number: "))
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

# for i in range(5, 16):
#     print(i)

# #list
# secore = [1, 41, 58, 9, 3]
# print(secore)
# #index
# # print(secore[4])
# print(secore[-1])
# print(secore[0])
# print(len(secore))
#
# for number in secore:
#     if number > 50:
#         print(number)

# #append remove pop

# #changing an item
# secore = [10, 20, 30, 40]
# secore[1] = 99
# print(secore)

# #adding item
# secore.append(50)
# print(secore)

# #remove by item
# secore.remove(30)
# print(secore)

# #remove by position
# secore.pop(0)
# print(secore)

# secore = [30, 50, 60, 70, 80]
# secore.append(100)
# secore.append(154)
# secore[1] = 20
# secore.pop(1)
# print(secore)
#
# print(len(secore))

# #secore[start : end)
# print(secore[0:3])
# print(secore[2:5])
# print(secore[:4])
# print(secore[4:])

# print(secore[-1])
# print(secore[-3])
# print(secore[-3:])

# data = [5, 12, 7, 25, 30, 18, 2, 40]
# print(data[0:4])
# print(data[-3:])
# print(data[2:6])

# number = [1, 2, 3, 4, 5]
# squared =[ x * x for x in number]
# # for x in number:
# #     squared.append(x*x)
# print(squared)

# #even
# even_squared = [ x * x for x in number if x % 2 == 0]
# print(even_squared)
#
# #odd
# odd_squared = [ x * x for x in number if x % 2 != 0]
# print(odd_squared)

# numbers = [ 1, 2, 3, 4, 5, 6]
# new_numbers = [ x for x in numbers if x > 3]
# print(new_numbers)
#
# multiplied = [x * 10 for x in numbers]
# print(multiplied)
#
# number1 = [ x * 10  for x in numbers if x > 3]
# print(number1)

# data = [3, 7, 10, 15, 20, 25]
# div_number = [ x * 2 for x in data if x % 5 == 0]
# print(div_number)



# #dict
# product = {"name" : "Ali", "price" : 12000, "stock" : "A"}
# product["category"] = "B"
# product["price"] = 11500
# print(product)
# for key, value in product.items():
#     print(key, value)
#
# # for key in product:
# #     print(key, product[key])

# # list of dict
# students = [
#     {"name" : "ali", "score" : 85},
#     {"name" : "ben", "score" : 92},
#     {"name" : "sara", "score" : 70},
# ]
#
# for student in students:
#     print(student["name"], student["score"])
#
# products = [
#     {"name" : "shoes", "price" : 85000, "stock": 3},
#     {"name" : "bag", "price" : 92000, "stock": 6},
#     {"name" : "ruler", "price" : 70000, "stock": 2},
# ]
#
# for product in products:
#     if product["price"] > 10000:
#         print(product["name"], product["price"])

# numbers = int(input("Enter a number: "))
# if numbers > 10:
#     print("Big")
# else:
#     print("Small")

# for i in range(1, 20):
#     if i % 2 == 0:
#         print(i)

# numbers = [5, 10, 15, 20, 25]
# print(numbers)
# print(type(numbers))
# print((numbers[0]))
# print((numbers[-1]))
# for number in numbers:
#     if number > 15:
#         print(number)

# numbers = [10, 20, 30]
# numbers.append(40)
# numbers.append(50)
# numbers[2] = 25
# numbers.pop(1)
# print(numbers)

# data = [5, 10, 15, 20, 25, 30, 35, 40]
# print(data[0 : 4])
# print(data[-3: ])
# print(data[2 : 6])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = [x for x in numbers if x % 2 != 0]
# print(odd_numbers)
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)
# multiplied = [x * 10 for x in numbers if x > 5]
# print(multiplied)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = [x for x in numbers if x % 2 != 0]
# print(odd_numbers)
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)
# multiplied =[x * 10 for x in numbers if x > 5]
# print(multiplied)

# number1 = int(input("Enter a number: "))
# number2 = int(input("Enter another number: "))
# if number1 > number2:
#     print("The number1 is greater than the number")
# elif number1 < number2:
#     print("The number2 is less than the number")
# else:
#     print("The number is equal to the number")

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
#
# if number1 > number2:
#     print("First is bigger")
# elif number2 > number1:
#     print("Second is bigger")
# else:
#     print("Equal")

# for number in range(1, 11):
#     if number % 3 == 0:
#         print("fizz")
#     else:
#         print(number)

# numbers = [2, 5, 8, 11, 14, 17, 20]
# count = 0
# for number in numbers:
#     if number > 10:
#         count +=1
#
# print(count)

# students = [
#     {"name": "Ali", "score": 85},
#     {"name": "Sara", "score": 92},
#     {"name": "John", "score": 70},
#     {"name": "Mina", "score": 95}
# ]
# count = 0
# for student in students:
#     if student["score"]> 80:
#         count +=1
# print(count)

students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "John", "score": 70},
    {"name": "Mina", "score": 95}
]
total = 0
for student in students:
    total += student["score"]
    average = total / len(students)
print(average)













