str = input("Enter a string; ")
string = ""
for i in str:
    if i.isalnum() or i.isspace() or i == "?":
        string += i
print(string)