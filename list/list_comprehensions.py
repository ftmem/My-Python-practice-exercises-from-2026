numbers = [1, 2, 3, 4, 5]
squared = [x * x for x in numbers]
even_squared = [x * x for x in numbers if x % 2 == 0]
odd_squared = [x * x for x in numbers if x % 2 != 0]
multiplied = [x * 10 for x in numbers if x > 3]
print(squared, even_squared, odd_squared, multiplied)