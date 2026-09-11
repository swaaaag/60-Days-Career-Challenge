print("LOGIN")

username=str(input("Enter the username: "))
password=str(input("Enter the password: "))
if username and password:
    if username=="user" and password=="password":
        print(f"WELCOME {username}.....")
    elif username!="user" or password!="password":
        print("USERNAME OR PASSWORD IS WRONG")
else:
    print("ENTER THE USERNAME & PASSWORD")