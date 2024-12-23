# Set = {} unordered and immutable, but ADD/REMOVE OK, NO duplicates

fruits = {"apple", "Orange", "Banana", "Coconut"}

print(fruits)



# Não é possível acessar o índice de elementos em um set 
# Unordered = print(fruits[0])

# Verifica o tamanho:
print(len(fruits))

# Remove um elemento do set:
fruits.remove("apple")

# Remove aleatoriamente um elemento:
fruits.pop()

# Verifica se um elemento está presente no set:
print("pineapple" in fruits)

# Add no set
fruits.add("pineapple")

# limpa o set:
fruits.clear()

