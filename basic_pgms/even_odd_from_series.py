num = int(input("Enter numbers : "))
even = 0
odd = 0
for i in num:
    if not i % 2:
        even += 1
    else:
        odd += 1
print("Total even numbers are " , even)
print("Total odd numbers are ", odd)