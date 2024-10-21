num = int( input("Enter a number : "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    rem = temp % 10
    sum += rem ** order
    temp //= 10
if num == sum:
    print(num,"is an ArmStrong Number")
else:
    print(num,"not an ArmStrong Number")
