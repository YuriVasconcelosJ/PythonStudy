import math

# C = 2*pi * R

# radius = float(input('Enter the radius: '))

# circumference = 2 * math.pi * radius
# print(f'The circumference is: {round(circumference, 2)}') 

# A = pi * r**2

# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is: {round(area, 2)}cm^2")

a = float(input('Enter side A: '))
b = float(input('Enter side B: '))

c = math.sqrt((pow(a, 2) + pow(b, 2)))

print(f"Side C = {c}")