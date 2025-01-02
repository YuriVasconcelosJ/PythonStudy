# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expresion for value in iterable if condition]

# A estrutura básica de uma list comprehension é:
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)


doubles_2 = [x * 2 for x in range(1,11)]
print(doubles_2)

fruits = ["apple", "orange", "banana", "coconut"]
uppercase_fruits = [fruit.upper() for fruit in fruits]

print(uppercase_fruits)

numbers = [1, -2, 3, -4, 5, -6]
positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num <= 0]

print(positive_numbers)
print(negative_numbers)
# numeros = [-3, -1, 0, 1, 2, 3, 4, 5, 6]

# numeros_pares = [numero for numero in numeros if numero % 2 == 0]
# print(numeros_pares)