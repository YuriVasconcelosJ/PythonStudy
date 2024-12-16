name = input("Enter your name:")

if len(name) >= 12:
    print("Invalid Name! (12>)")
elif not name.isalpha():
    print("Invalid Name (Number)")
# O find, retorna a posição daquela letra(-1 é true)
# elif name.find(" "):
elif " " in name:
    print("Invalid Name (space)")
else:
    print("Name valid")