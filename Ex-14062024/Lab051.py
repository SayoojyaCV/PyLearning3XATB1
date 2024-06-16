#Break - to come out of the loop based on a condition

#pass - do nothing and skip the code

# for i in range(10):  #0 to 9
#     print(i)
# for i in range(0,10):  #0 to 9 , same as above
#     print(i)
for i in range(10):  #0 to 9
    if i == 5 or i == 6:
        pass
    else:
        print(i)
