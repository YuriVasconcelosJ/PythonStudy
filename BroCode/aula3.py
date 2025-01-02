# TypeCasting:  Process of converting a variable from one data type to another type
#               str() int() float(), bool()
# TypeCasting: Processe de converter uma variável de um tipo de dado para outro.

# Declaração de variáveis
name = "Bro Code"
age = 25
gpa = 3.2
is_student = True

# Tipo da variável antes da conversão
print(f"O tipo de 'gpa' antes da conversão é{type(gpa)}")

# Convertendo gpa de float para int
gpa = int(gpa)
print(type(gpa))

# Tipo da variável antes da conversão
print(f"O tipo de 'gpa' antes da conversão é{type(age)}")

# Convertendo gpa de float para int
age = str(age)
print(type(age))

print(bool(name))