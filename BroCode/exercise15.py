import random as rd
# Laço de repeticao-> Ate o user escrever corretamente a merda da opcao que estiver listada entre as 3 -> Verificar e seleicionar para entrar nos condicionais
# Tupla
options = ("rock", "paper", "scissors")

print('-' * 30)

while True:
    user = input("Enter a option:[rock, paper, scissors]: ").lower().strip()
    if user not in options:
        print('Digite uma opção correta')
        continue
    break
# Opções:
computer = rd.choice(options)

# Exibir escolhas
print('-' * 30)
print(f"Você escolheu: {user}")
print(f"O computador escolheu: {computer}")
# Condições:
# Empate
if computer == user:
    print('Empate!')
# Condição de vitória
elif (user == 'rock' and  computer == 'scissors') or \
     (user == 'paper' and  computer == 'rock') or \
     (user == 'scissors' and  computer == 'paper'):
      print("Você ganhou!")
# Derrota
else:
     ("Você perdeu")
