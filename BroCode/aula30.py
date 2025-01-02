# Iterables = An object/collection that can return its elements one at time
#             allowing it to be iterated ove in a loop

# Se um objeto pode ser percorrido em um loop for, ele é considerado um iterable
# Strings, Listas, Tuplas, Dicionários, Conjuntos(sets), geações criadas por funções range() e zip()

# 
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# Exemplo de Iterable e Iterador:

lista = [1, 2, 3]  # Iterable
iterador = iter(lista)  # Obtém um iterador do iterable

print(next(iterador))  # Saída: 1
print(next(iterador))  # Saída: 2
print(next(iterador))  # Saída: 3
# print(next(iterador))  # Erro: StopIteration (não há mais elementos)

# Iterator
# É o objeto que faz a iteração real.
# Implementa o método __next__(), que retorna o 
# próximo elemento ou levanta StopIteration quando não há mais elementos.