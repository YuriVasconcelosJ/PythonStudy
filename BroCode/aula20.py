# Collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. 
#   Set = {} Unordered and immutable, but Add/Remove OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. Faster

# Maneiras de criar uma lista, Set ou tupla:
list1 = []
#  OR
list1 = list()
# Add vários itens a lista
list1.extend(("Yuri", "Felipe", "Ranny"))
# print(list1)
# Lisat simples  
fruits = ["apple", "orange", "banana", "coconut"]
# print(fruits[2])
# Verifica o tamanho da lista:
len(fruits)
# Verifica os métodos disponiveis:
#print(help(fruits))
for fruit in fruits:
    pass
#    print(fruit)

# Inseri o elemento na posição desejada pelo user:
list1.insert(1, "gama")
print(list1)

# Inseri o elemento ao final da lista:
list1.append("Corra")
print(list1)

# Remove um elemento da lista especificament o elemento que você deseja remover:
list1.remove('Corra')
print(list1)

# Verifica quantos elementos tem na lista(Duplicados)
list1.count()

# Verifica se aquele elemento está presente na lista:
print("Felipe" in list1)
print("Matheus" in list1)
