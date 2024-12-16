# String Methods

name = input("Enter your full name:")

# Tamanho da string
result = len(name)

# Procura e retorna a primeira ocorrência da letra
result = name.find("y")

# Procura e retorna a última ocorrência de uma letra
result = name.rfind("r")

# Deixa a primeira letra da string maiúscula
name = name.capitalize()

# Deixa todas as letras maiusculas
name = name.upper()

# Deixa todas as letras minúsculas
name = name.lower()

# Verifica se contem apenas números
name = name.isdigit()

# Conta quantas vezes uma determinada caractere aparece
result = name.count("")

# Troca um caractere por outro
result = name.replace("y","x")
print(result)
