print('....SUM OF NUMBERS....')

num=list(map(int, input('Enter the numbers seperated by space: ').split()))
sum=0
for i in num:
    sum=sum+i
print(f'The sum of numbers is ...{sum}...')