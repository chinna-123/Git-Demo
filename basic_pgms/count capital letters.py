str = input("Enter a string:")
count = 0
for char in str:
    if char.isupper():
        count += 1
print("Number of capital letters in a given string is :",count)