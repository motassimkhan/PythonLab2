a=int(input("number1:\n"))
b=int(input("number2:\n"))
c=int(input("number3:\n"))
if a==b==c:
    print("all are equal")
elif a==b:
    if c>a:
        print(f"{c} is greatest")
    else:
        print(f"{a} and {b} are equal")
elif b==c:
    if a>b:
        print(f"{a} is greatest")
    else:
        print(f"{b} and {c} are equal")
elif a==c:
    if b>c:
        print(f"{b} is greatest")
    else:
        print(f"{c} and{a} are equal")
else:
    if a>b and a>c:
        print(a,"is greatest")
    elif b>a and b>c:
        print(b,"is greatest")
    elif c>a and c>b:
        print(c,"is greatest")
    else:
        print("give proper input")
