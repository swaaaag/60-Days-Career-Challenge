print('.....PYRAMID.....')

row=int(input('Enter the rows of pyramid: '))
for i in range(1, row+1):
    for j in range(1, 2*i):
            print("*", end="")
    print()
    