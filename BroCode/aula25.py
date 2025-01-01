import time

# Valor padrão - Fica um valor padrão no parâmetro, fazendo com que não seja necessário informar o valor no argumento 
def count(end ,start=0):
    for x in range (start, end+1):
        print(x)
        time.sleep(1)
    print('DONE!')

count(0, 10)