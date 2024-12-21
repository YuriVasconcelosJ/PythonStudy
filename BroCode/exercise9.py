import time

my_time = int(input("Enter the time:"))

# Laço de repetiçao para contar de 0 a até o tempo definido pelo tempo
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) # % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME IS UP!")