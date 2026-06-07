def gratest(a,b,c):
    if a>b and a>c:
        return f"A  {a}"
    elif b>a and b>c:
        return f"B {b}"
    else:
        return f"C {c}"
a=int(input("enter your number A:"))
b=int(input("enter your number B:"))
c=int(input("enter your number C:"))
print(f"the gratest number is:{gratest(a,b,c)}")