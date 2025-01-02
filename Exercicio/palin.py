palavra = input('Digite uma palavra:')

if palavra == palavra[::-1] :
    print("Palíndromo")
else:
    print('Não é um palin')