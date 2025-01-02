# *args (Argumentos Posicionais Arbitrários)

# O *args permite que você passe um número arbitrário de argumentos posicionais para uma
# função. Esses argumentos são empacotados em uma tupla.

# *args coleta todos os argumentos posicionais passados para a função.
# Ele trata os argumentos como uma tupla.
def somar(*args):
    return sum(args)

print(somar(1, 2, 3, 4))  # Saída: 10

# Iterando sobre um *args

def imprimir_args(*args):
    print(type(args))
    for arg in args:
        print(arg)

imprimir_args("Python", "é", "incrível")
# Saída:
# Python
# é
# incrível

# O **kwargs(Argumentos Nomeados Arbitrários) 

# O **kwargs permite que você passe um número arbitrário de argumentos nomeados (chave-valor) para uma função.
# Esses argumentos são empacotados em um dicionário.

def mostrar_informacoes(**kwargs):
    print(type(kwargs))
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_informacoes(nome="Alice", idade=25, cidade="São Paulo")
# Saída:
# nome: Alice
# idade: 25
# cidade: São Paulo

# **kwargs coleta todos os argumentos nomeados passados para a função.
# Ele os organiza como pares de chave-valor em um dicionário.

def exibir_detalhes(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)

exibir_detalhes(1, 2, 3, nome="João", idade=30)
# Saída:
# Argumentos posicionais: (1, 2, 3)
# Argumentos nomeados: {'nome': 'João', 'idade': 30}

def display_name(*args):
    """
    Função para pegar varíos elementos não nomeados e juntar eles em uma string
    """
    name = ""
    for arg in args:
        name = name + " " + arg 
    # Remove todo o espaço inicial e final
    return name.strip()
    # Segunda maneira utilizando o método join()
    return " ".join(args)
    

name = display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
print(name)
