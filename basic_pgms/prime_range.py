n1 = int(input("Enter stating range : "))
n2 = int(input("Enter ending range :"))

for i in range(n1,n2+1):
    for j in range(2,i):
        if ( i % j ) == 0:
            break
    else:
        print(i)