# neasted loops

rows = int(input("Entre the number of rows:"))
columns = int(input("Enter the number of columns:"))
symbol = input("Enter the symbol:")


for x in range(columns):
    for y in range(rows):
        print(symbol, end=" ")
    print()

# for y in range(3):
#     for x in range(1, 11):
#         print(x, end=" ")
#     print()