#Assignment operator
#- - assign the value to the right
name = "John"
print(name)

#== - Compare operator (bool)
v1 = (1 == True)
v2 = (0 == False)
print(v1)
print(v2)

age = 65
print(age)
age = +65  #unary operator - Pycharm removes automatically since self explanatory
print(age)
num = -1
print(num)
r = age + num  #BODMAS rule
print(r)
r1 = age - num
print(r1)

#Not operator (Boolean)
is_married = True
print(is_married)
print(not is_married)

#Is operator - identity operator (bool) , mostly used in case of lIst

a = 5
b = 6
c = False
print(a is b)

my_list = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 3, 4, 5]
print(my_list is my_list2)  #both are stored separately so doesnt match

