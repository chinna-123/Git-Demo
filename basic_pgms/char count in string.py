# using count 90 method
str = input("Enter a string : ")
string = str.upper()
list = [ ]
for ch in string:
    if ch not in list:
        list.append(ch)
        print(string.count(ch),"times", ch ,"repeated")

# without using count()
print(hye)