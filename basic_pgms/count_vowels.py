str = input("Enter a string:")
string = str.lower()
count = 0
list = ['a','e','i','o','u']
for char in string:
    if char in list:
        count += 1
print("Number of vowels in a given string is :",count)