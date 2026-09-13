print('....FACTORIAL OF A NUMBER....')

num=int(input('Enter the number to find the factorial: '))
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print(f'Factorial {num}! is ...{fact}')