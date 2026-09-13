print('.....PRIME NUMBERS.....')

num=int(input('Enter the number of limit: '))
prime=[]
for n in range(2, num+1):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            break
    else:
        prime.append(n)
print(prime)