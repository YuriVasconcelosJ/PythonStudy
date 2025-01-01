# Keyword arguments = an argument preceded by an identifier helps with readbility order of arguments
#                     arguments doesn't matter

def hello (gretting, title, first, last):
    print(f"{gretting} {title} {first} {last}")

hello("Hello", title="Mr.", last="Squarepants", first="Spongeboob")
hello("Hello", title="Mr.", first="James", last="John")


