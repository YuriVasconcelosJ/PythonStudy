# Crescente
for x in range(1, 10):
    print(x)

print('-' * 10)
# Decrescente
for x in reversed(range(1, 10)):
    print(x)
    
print('-' * 10)
# Pulando números:
for x in range(1, 10, 2):
    print(x)

print('-' * 10)
# Crescente
for x in range(1, 10, 2):
    print(x)

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)