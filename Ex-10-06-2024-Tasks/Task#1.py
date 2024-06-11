#Question1
#Explain the difference between the = operator and the == operator in Python.
#= operator
Harry_marks = 90
Tom_marks = 99
print(Harry_marks)
print(Tom_marks)
a = Harry_marks + Tom_marks
print(a)

#==operator
a=10
b=20
print(a==b) # prints false since value of a is not equal to value of b

a=25
b=25
print(a==b) # prints true since value of a is equal to value of b

#Question2
#What does the ** operator do in Python, and how is it used?
#** represents power of a value
a=2
b=a**2
print(b)
a1=3
b1=a1**2
print(b1)
b2=a1**3
print(b2)

#Question3
#What does the ^ operator do in Python, and in what context is it commonly used?
# ^ is an Exclusive OR operator
a=2
b=4
print(a^b)
