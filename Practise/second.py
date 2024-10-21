stri = "Just do it!"
print(stri[10])      # prints !
print(stri[5:7])     # prints do
print(stri[8:11])    # prints it!
print(stri[:4])      # prints Just
print("Don't" + stri[4:])          # prints Don't do it!

var = 1.53
print(type(var))
print(str(var) + " is a float.")

print("*******\n*****\n***\n*")

# input function

name = input("Enter your name ")
print("Your name is " + name + ".")
print(type(name))

fav_num = input("Enter ur fav number ")
print("Your fav number is " + fav_num + ".")
print(type(fav_num))

fav_num = int(input("Please Enter an integer number "))
print(fav_num)
print(type(fav_num))

# Assignment

use_int = int(input("Please enter an integer."))

print(use_int + 10)


use_int = input("Please enter an integer.")

print(int(use_int) + 10)