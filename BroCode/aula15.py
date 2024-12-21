# Indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "123-456-789"

# Retorna apenas um caractere
print(credit_number[1])

# Retorna uma determinada parte da string fatiada
print(credit_number[0 : 4])

# Retorna do caractere selecionado até o final
print(credit_number[2 : ])

# Retorna uma ordem inversa
print(credit_number[-1])

# Retorna os caracteres 2 em 2
print(credit_number[::2])