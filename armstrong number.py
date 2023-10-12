n = int(input("Enter number: "))
arm = 0
while n>0:
    rem = n%10
    arm = arm+ (rem*rem*rem)
    n//=10
print(arm)
    
