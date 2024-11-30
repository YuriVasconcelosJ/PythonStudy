# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe me JSON
# e depois cire novamente as instâncias
# da classe com os dados salvos
# Façam em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula127.json'

# Lista vazia
lista_pessoa = []

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("João", 20)
p2 = Pessoa("Luiz", 20)
p3 = Pessoa("Renata", 15)

lista_pessoa = [p1.__dict__, p2.__dict__, p3.__dict__]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(lista_pessoa, arquivo, ensure_ascii=False, indent=2)
