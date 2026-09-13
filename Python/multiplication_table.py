print("MULTIPLICATION TABLE\n")

num=int(input('Enter a number for multiplication table: '))
lim=int(input('Limit of the table: '))
i=1
while i<=lim:
    print(f"{i} x {num} = {num*i}")
    i+=1