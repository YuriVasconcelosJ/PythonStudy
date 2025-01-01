# function - A block reusable code
#            place () after the function name to invoke it

# def saudacao(nome):
#     print(f"Olá, {nome}!")


# saudacao('Yuri')

# Funções com sem retorno (None):
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday(18, 'Bro')
happy_birthday(30,'Carl')
happy_birthday(17, 'Maria')

# Funções com Retorno (Return):

def somar(a, b):
    return a + b

# Maneiras de retornar uma função 
resultado = somar(5, 4)
print(somar(5,4))  

# Parâmetros: são variáveis definidas na declaração da função. Posicionais(Ordem importa), Padrão(Valor padrão)
# Argumentos são os valores passados para a função durante a chamada.

def create_name(first, last):
    '''
    Função que chama o nome e sobrenome como parametro e transforma a inicial das letras em uppercase 
    '''
    first = first.capitalize()
    last = last.capitalize()
    return  first + " " + last

full_name = create_name('yuri', 'vasconcelos')
print(full_name)