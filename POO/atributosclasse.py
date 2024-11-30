class Carro:
    # Atributo de classe
    rodas = 4  # Todas as intancias compartilham esse valor

    # Método construtor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Acessando pela classe

print(Carro.rodas) # Sáida: 4

# Acessando pela instância
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

print(carro1.rodas) # Sáida: 4
print(carro2.rodas) # Sáida: 4

# Modificando pela classe 
Carro.rodas = 6
print(carro1.rodas)  # Saída: 6
print(carro2.rodas)  # Saída: 6