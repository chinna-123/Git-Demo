def sum(x,y):
    s = x+y
    print("sum of two numbers is :", s)

sum(20,30)  #sum of two numbers is : 50

#======
def fun(x,y):
    print("x+y",x+y)
    return x+y
fun(2,3)
#====
def greet(Aadi):
    print("Hello, " + Aadi + ". Good morning!")
greet('Aadi')

#=======
tuple = ()
print(tuple)
tuple = (1,2,3)
print(tuple)
tuple = (1,"helo",3,4,'adi')
print(tuple)
tuple = 1,2,'dog'
print(tuple)
tuple = ('mouse',[1,2,3],(4,5,6))
print(tuple)
a,b,c = tuple
print(a)
print(b)
print(c)
tuple = ('helo')
print(type(tuple))
tuple = ('helo',)
print(type(tuple))
tuple = 'helo',
print(type(tuple))
tuple = 5,
print(type(tuple))
tuple = ['a','b','c','d','e','f']
print(tuple[-6])
tuple = ('mouse',[1,2,3],(4,5,6))
print(tuple[1][1])
tuple = ('a','e','i','o','u','s')
print(tuple[1:4])
print(tuple[:])
print(tuple[:-3])
print(tuple[3:])

#def sum(arg1, arg2)
def add(a,b):
    print("a+b",a+b)
    return a+b
def msg():
    print('hello')
    return
add(10,202)
msg()

#====
def fib(n):
    a,b = 0,1
    while a<n:
        print(a, end='  ')
        a , b = b ,a+b
    print()
fib(10)

#===
def greet(name):
    print("Hello, " + name + ". Good morning!")
greet("Aadi")




