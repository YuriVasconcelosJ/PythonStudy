import random

def get_integer_input():
    while True:
        user_input = input("Digite um número inteiro: ")
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_runnig = True

print('Python Number Guessing')
print('-' * 40)
print(f'Select a number between {lowest_number} and {highest_number}')

while is_runnig:

    guesses = get_integer_input()
    # Verifica se o númeor está dentro do limite de 0 a 100
    if guesses < lowest_number or guesses > highest_number:
        print('The number is out of range')
        print(f'Select a number between {lowest_number} and {highest_number}')
    # Verifica se o número sorteado e maior
    elif guesses < answer:
        print('Too high! Try again')
        print(f'Select a number between {lowest_number} and {highest_number}')
    # Verifica se o número sorteado e menor
    elif guesses > answer:
        print('Too low! Try again')
        print(f'Select a number between {lowest_number} and {highest_number}')
    # Conição de estar correto 
    else:
        print('Correct!')
        print(f'The number is {guesses}')
        is_runnig = False
