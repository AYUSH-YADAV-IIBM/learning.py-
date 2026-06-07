<<<<<<< HEAD
num1=float(input("enter your 1st number: "))
num2=float(input("enter your 2nd number: "))
print("salect your operaters:[+ - * /]")
op=input("enter your operaters:")
if op=="+":
    print("the result is:",num1+num2)
elif op=="-":
    print("the relult is:",num1-num2)
elif op=="*":
    print("the result is:",num1*num2)
elif op=="/":
    if num2 !=0:
        print("the result is:",num1/num2)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("error: wrong operater")
=======
num=float(input("enter first number:"))
num2=float(input("enter secound number:"))

print("srlect your operater:[+,-,*,/]")
op=input("enter your operater")

if op=="+":
    print(f"you choose: {op}")
    print("your addition is",num+num2)

elif op=="-":
    print(f"you choose:{op}")
    print("your subtraction is:",num-num2)

elif op=="*":
    print(f"you choose:{op}")
    print("your multiply is:",num*num2)

elif op=="/":
    if num2!=0:
       print(f"you choose:{op}")
       print("your divide is:",num/num2)
    else:
        print("error becoz divide zero is not allow")
else:
    print(f"you choose wrong {op} operater")

>>>>>>> e12166d (add)
