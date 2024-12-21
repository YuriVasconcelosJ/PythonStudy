# while loop = execute some code WHILE some condition remains TRUE

# Executa uma condição enquanto ela for verdadeira

name = input("Enter your name: ")

while name == "":
    print("You didnt enter your name.")
    name = input("Enter your name: ")

print(f"Hello {name}!")

food = input("Enter your favorite food:")

while not food == "q":
    print(f"I like {food}")
    food = input("Enter your favorite food:")

print("bye")