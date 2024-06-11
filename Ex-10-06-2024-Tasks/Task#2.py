# Develop a Python script that calculates the square and cube of a given number.
# num = 2 sq - 4, c = 8

import math

num = 2
a = num ** 2
print(a)  #prints the square of num - Method 1

a1 = math.pow(num, 2)  #prints the square of num - Method 2
print(a1)

a2 = float(input("Enter a value to calculate the square\n"))
b2 = math.pow(a2, 2)
print(b2)
print("Square of a2=", b2)  #prints the square of num - Method 3

c = math.pow(num, 3)
# print("Value of c is", c)  #prints the cube of num - Method 1
print("Cube of num is", c)  #prints the cube of num - Method 1

c2 = float(input("Enter a value to calculate the cube\n"))
Cube_value = math.pow(c2, 3)
print("Value of cube is", Cube_value)  #prints the cube of num - Method 2

#********************************************************************************
# Question2
# # Create a program that takes two numbers as input and prints whether the first number
# # is greater than, less than, or equal to the second number.

First_num = float(input("Enter the first number F:\n"))
Sec_num = float(input("ENter the sec number S:\n"))
print("First number is greater than second number", First_num > Sec_num)
print("First number is lesser than second number", First_num < Sec_num)

First_num = float(input("Enter the first number A:\n"))
Sec_num = float(input("Enter the sec number B:\n"))
A = First_num
B = Sec_num
if (A > B):
    print("A is greater than B")
else:
    print("B is greater than A")

First_num_equal = float(input("Enter the first number x:\n"))
Sec_num_equal = float(input("Enter the sec number y:\n"))
x, y = First_num_equal, Sec_num_equal
if (x == y):
    print("First number is equal to Second number")
else:
    print("Both are different")
