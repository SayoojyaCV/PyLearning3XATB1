#Conditions and Loops
#++ and -- does not exist in Python

#age>18 # you are allowed
#age<18 # you are not allowed


#if , else
# #Syntax for if else
# if condition:
#     code to be executed
# else:
#     code to be executed when condition is false

#Write a program to take a user input and let him know if he is allowed

age = int(input("Enter your age:\n"))
if age > 18:
    print("Go to the club")
else:
    print("Not allowed")
