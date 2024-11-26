class Carro:
    # Método construtor
    def __init__ (self, modelo="generico", ano=2020):
        self.modelo = modelo
        self.ano = ano

# Valores padrão
carro1 = Carro()
print(carro1.modelo)

# Valores criado
carro2 = Carro("Sedan", 2022)
print(f"O modelo do carro é: {carro2.modelo}")
