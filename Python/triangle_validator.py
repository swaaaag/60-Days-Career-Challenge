print("TRIANGLE VALIDATOR")

p=int(input("Enter the side P : "))
q=int(input("Enter the side q : "))
r=int(input("Enter the side r: "))

if p+q>r and p+r>q and q+r>p:
    print("valid triangle..!!!!\n")
    if p==q==r:
        print("This is an EQUILATERAL TRIANGLE")
    elif p==q or q==r or p==r:
        print("This is an ISOSCELES TRIANGLE")
    else:
        print("This is a SCALENE TRIANGLE")
else:
    print("THIS IS AN INVALID TRIANGLE...!!!")