# Shopping cart program

foods = []
prices = []
total = 0


while True:
    food = input("Enter a food to buy (q to quit):")
    if food.lower() == "q":
        print("Finish program")
        break
    price = float(input(f"Enter the price of a {food}:$"))
    foods.append(food)
    prices.append(price)
    # Primeita maneira de calcular o total
    # total += price

print("-" * 4, "YOUR CART", "-" * 4)

for food in foods:
    print(food)

# Segunda maneira de calcular o total:
for price in prices:
    total += price

print(f"Your total is: {total}") 