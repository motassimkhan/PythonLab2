'''
age = int(input("Enter your age: "))
if age>=18:
    print(f"you are eligible to vote")
else:
    print("Dont vote")
'''
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fact(num-1)

ele = int(input("enter number: "))
facto = fact(ele)
print(f'The factorial of {ele} is {facto}')
