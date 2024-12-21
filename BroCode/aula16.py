# Format specifiers = {Value :flags} format a value based on what 
#                     flags are inserted

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 1000000

# Colocando casas decimais:
print(f"Price 1 is: {price1:.2f}")
print(f"Price 2 is: {price2:.2f}")
print(f"Price 3 is: {price3:.2f}")

# Colocando mais de casas decimais presentes:
print(f"Price 1 is: {price2:010f}")

# Coloca 10 caracteres após os caracteres
print(f"Price 1 is: {price1:<10}")

# Coloca 10 caracteres antes dos caracteres
print(f"Price 1 is: {price1:>10}")

# Coloca 10 caracteres no meio dos caracteres
print(f"Price 1 is: {price1:^10}")

# Coloca o caractere positivo ou negativo no início:
print(f"Price 1 is: {price1:+}")

# Coloca vírgula entre os caracteres:
print(f"Price 1 is: {price4:,}")

