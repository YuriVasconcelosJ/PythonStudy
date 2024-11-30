class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando uma instância
p = Pessoa("Ana", 25)

# Exibindo os atributos como um dicionário
print(p.__dict__)
# Saída: {'nome': 'Ana', 'Idade': 25}

# Modificando os atributos via __dict__
p.__dict__['idade'] = 30
print(p.idade) # Sáida 30

# Adicionando novos atributos
p.__dict__['Cidade'] = "São Paulo"
print(p.cidade) # Saída: São Paulo

class Carro:
    # Atributo da classe
    rodas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Acessando __dict__ na classe
print(Carro.__dict__)
# Saída Dicionário com informações sobre 'rodas', métodos e metadados da classe

