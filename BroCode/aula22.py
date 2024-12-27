fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# Como acessar um elemento de uma lista que está dentro de outra lista
print(groceries[2][0])
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
