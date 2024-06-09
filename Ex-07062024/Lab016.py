# Take 2 int numbers from user and add them
# we need to use input function to take input from user
num1 = input("Enter your first number")
num2 = input("Enter your second number")
#result=num1+num2
# -- results in concatenation sp prints result as 9091
#print(result)
# type function conversion str--> int

# int - sum() - int+int
# str - concatenation - str+str

result =int(num1) + int(num2)
print(result)

# int to str - str()
# str to int - int()

print(type(int(num1)))
