#Program - calculate area of a circle
#input = radius
#output = area

#data types
#input = int or float --> float
#output = float

#COre  logic = pi * r * r =3.14 * r * r
#math.pi = 3.14 - math.pi will give the value of pi

radius = input("Enter the radius of the circle:\n ")
radius= float(radius)

# or
radius = float(input("Enter the radius of the circle:\n "))
import math
print(math.pi)
area=math.pi*(radius**2)
area2=math.pi*(math.pow(radius,2))
print(area)
print(area2)