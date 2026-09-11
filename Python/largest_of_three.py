num1, num2, num3=map(int,input("Enter three numbers: ").split())
if num1>num2 and num1>num3:
    print(f"{num1} is the largest of three")
elif num2>num3:
    print(f"{num2} is the largest of three")
else:
    print(f"{num3} is the largest of three")