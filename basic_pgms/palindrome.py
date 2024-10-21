str = input("Enter a string: ")
revstr = (str[::-1])
if revstr == str:
    print("palindrome")
else:
    print("not a palindrome")