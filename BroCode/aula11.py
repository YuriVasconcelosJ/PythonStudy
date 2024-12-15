# Logical Operators - evalute multiple codintions (or, and, not)
#                     or - at least one  condition must be true
#                     and - both conditions must be true
#                     not - inverts the condition (not False, not True)
# Order of Precedence = Not And Or 

temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is COLD oustide")
    print("It is Sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")