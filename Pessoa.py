class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto da classe pessoa
pessoa = Pessoa("Ana", 25)

print("Acessando os dados dentro da classe pessoa:")
print(pessoa.nome)
print(pessoa.idade)