
id = input("ID: ")
pwd = input("Password: ")

if id != "admin":
    print("Invalid ID")
else:
    if pwd == "1234":
        print("Login Sucess")
    else:
        print("Wrong Password")
