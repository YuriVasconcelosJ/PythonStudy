# module = a file containing code you want to include in your program
#          use 'import' to include a module (buillt-in or your own)
#          useful to break up a large program reusable separate files

# Importando um módulo
# import math

# Importando um módulo e colocando um nome para ele
import math as m

# print(math.pi)

# print(m.pi)

# Diferença entre import math X from math import * 

# O import math importa o módulo inteiro, mas a gente é obrigado a utilizar o: math.<nome da funcao>
# O from math import * importa o módulo inteiro, mas a gente utiliza a função/métodos diretamente: sqrt() 

# Geralmente a gente utiliza from math import sqrt, pi