print("LEAP YEAR CALCULATOR\n")

year=int(input("Enter an year: "))
dup=year
year=year%4
if year==0:
    print(f"{dup} is a LEAP YEAR!!!")
else:
    print(f"{dup} is not a LEAP YEAR")
