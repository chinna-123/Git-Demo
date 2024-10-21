a = 0
b = 1
print(a)
print(b)
print("-----")
for i in range(2,10):
    c = a + b
    print(c)
    a = b
    b = c
