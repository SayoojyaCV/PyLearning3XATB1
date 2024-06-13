# # ✅ #4. Fibonaci series
# # 0,0+1, 0+1+1,
# # n = 7
# # 0, 1, 2, 3, 5, 8, 13
#
n = int(input("Enter a number:\n"))
a, b = 0, 1
for i in range(0, n + 1):
    c = a + b
    a = b
    b = c
print(c)
# x = list(range(c))
# print(x)
