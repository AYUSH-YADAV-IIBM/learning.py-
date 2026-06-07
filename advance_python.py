# walrus operater
#use:
if(n:=len([1,2,3,4,5]))  >3:
    print(f"list is to long:{n} element expected <=3")
    # ye method code kon short bana deta hain


# type of defination in pyton
age:int=25
print(age)

def greeting(name:str,surname:str) -> str:
    return F"HELLO:\t{name}\t{surname}"
print(greeting("AYUSH","YADAV"))