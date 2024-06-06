# Program to find max of two numbers
max(100, 200)
print(max(100, 200))
print(max(100, 200, 999))
print(max(100, 200, 555, 678, 8999))
print(max(100, 200, 555, 678, -1, -3, 1.1, 999.99))
# TypeError: '>' not supported between instances of 'str' and 'float'
# words and float cannot be combined together in this case
print(max(100, 200, 555, 678, -1, -3, 1.1, 999.99, "word"))
