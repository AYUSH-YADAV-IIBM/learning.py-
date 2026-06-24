correct_username="ayush yadav"
correct_password=12345

username=input("enter your username:")
password=int(input("enter your password:"))

if username==correct_username or password==correct_password:
    print("login sucessful")

else:
    print("error:please enter valid username and password")