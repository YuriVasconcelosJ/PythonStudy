# Variables - Armazenar conteúdo dentro de uma variavel
first_name = "Bro"
food = "Pizza"
email = "Brocode@fake.com"

print(first_name)

# Exibindo informçãoes báiscas
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"My email is {email}")

# Inteiros
quantity = 3
age = 25

# Diferente: Uma string representando um número
age_string = "25"

# Verifica o tipo daquela variável 
print(type(age))    # <class 'int'>
print(type(age_string)) # <class 'str'>

# Float
price = 10.99
print(type(price))  # <class 'float'>

# Booleano
condition = True # Camel case não é utilizado em Python
print(type(condition))

# Condicional usando booleano
if condition:
    print('Verdade!')
else:
    print("Falso!")