# #leap year checker
# ✅ 1. Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
#
#
#
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#
# Use an if-else statement to make this determination.

Year = int(input("Enter a year:\n"))
print(Year)
a = Year % 4
b = Year % 400
c = Year % 100

if (a == 0) or (b == 0):
    if (c != 0):
        print("Leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")
