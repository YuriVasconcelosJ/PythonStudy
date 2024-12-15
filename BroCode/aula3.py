# TypeCasting:  Process of converting a variable from one data type to another type
#               str() int() float(), bool()

name = "Bro Code"
age = 25
gpa = 3.2
is_student = True

print(type(gpa))
gpa = int(gpa)
print(type(gpa))

age = str(age)
print(type(age))

print(bool(name))