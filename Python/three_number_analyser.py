print("THREE NUMBER ANALYSER")

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

#largest number

if num1>num2 and num1>num3:
    print(f"The largest number is {num1}")
elif num2>num3:
    print(f"The largest numebr is {num2}")
else:
    print(f"The largest number is {num3}")

#smallest number

if num1<num2 and num1<num3:
    print(f"The smallest number is {num1}")
elif num2<num3:
    print(f"The smallest number is {num2}")
else:
    print(f"The smallest number is {num3}")

#whether two equal or not

if num1==num2 and num1==num3:
    print("All three are Equal!!!")
elif num1==num2:
    print(f"{num1} and {num2} are equal")
elif num1==num3:
    print(f"{num1} and {num3} are equal")
elif num2==num3:
    print(f"{num2} and {num3} are equal")
else:
    print("All three is different")

