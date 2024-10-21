# we can use same name for d/f variables as long as
# they are in d/f scopes


def local_ex1():
    fruit = "apple"
    print(fruit)


def local_ex2():
    fruit = "banana"
    print(fruit)


fruit = "jamkaya"
local_ex1()
local_ex2()
print(fruit)