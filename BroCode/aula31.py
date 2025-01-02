# Membership Operators = Used to test whether a value or variables is found ia a sequence
#                        (String, List ,Tuple, Set, or Dictionary)
#                         1. In
#                         2. Not In

word = "APPLE"

letter = input("Guess a letter in the secret word: ").upper()

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

# Verificação email
email = "BroCode@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")