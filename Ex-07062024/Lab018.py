# Strings
# Bunch of char
# '', "", """ """
name = 'Harry'
print(name)
name = "Harry"
print(name)

name = """Harry loves pets
...
...
..."""
print(name)

# dir="C:\nomedir\some dir"
print(dir)
# \n in the string will be considered as a new line and it will print in new line..
# so to solve that we need to add raw before the dir name

# r=raw string
dir = r'C:\nomedir\some dir'
print(dir)

# Format of the string
first_name = "Harry"
last_name = "Potter"
print(first_name, last_name)
print(first_name + " " + last_name)
print(first_name + "" + last_name)

# f-formatting - it will replace the values of variables
# {} - place holders
print(f'Your Full name is {first_name} {last_name}')
