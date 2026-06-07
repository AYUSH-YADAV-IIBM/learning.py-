#opps:1st
class employee:
    company="itc"
    name="ayush"
    def show(self):
        print(f"name of the employee:{self.name}\n name of the company is:{self.company}")


class programmer(employee):# programmer ke andar employee ka v detils aa gya 
    company="itc infotech"
    lang="python"
    def showlang(self):
        print(f"name of the company is{self.company}\n name:{self.name}\n good with:{self.lang}language")

a=employee()
a.show()
b=programmer()
b.showlang()


#multiple inhertance
#1st employee
#2nd coder
#3rd programmer(employee,coder)
class employee:
    company="itc"
    name="aniket"
    def show(self):
        print(f"the name of employee:{self.name}\n the name of company:{self.company}")
class coder:
    lang="python"
    def lan(self):
        print(f"your language is:{self.lang}")
class programmer(employee,coder):
    company="ayush tech"
    def  showall(self):
     print(f"the name is:{self.name}\n the company name is:{self.company}\n he is good with:{self.lang}")
a=employee()
a.show()
b=coder()
b.lan()
c=programmer()
c.showall()

#multilevel inheritance
#employe
#programmer
#manager
class employee:
    company="tcs"
    def em(self):
        print(f"the company name is:{self.company}")
class programmer(employee):
    language="python"
    def lang(self):
        print(f"the company name:{self.company}\n the language is:{self.language}")
class manager(programmer):
    level="advance"
    def all(self):
        print(f"the comapny name is:{self.company}\n language is:{self.language}\n level is:{self.level}")

a=employee()
a.em()
b=programmer()
b.lang()
c=manager()
c.all()


# also we can overwrite or add new artibutes and method in programmmer class
class employee:
    company="itc"
    name="ayush"
    salary=5000

    def show(self):
        print(f"the name of employee is:{self.name} and salary is:{self.salary}")

class programmer(employee):
    company="infotech"
    name="aniket"
    language="python"

    def showlang(self):
        print(f"the name is :{self.name} he is good with {self.language}")

ep1=employee()
ep1.show()

ep2=programmer()
ep2.show()
ep2.showlang()



#super method help karta hain bina call kea pafrents ko v call karna
class employee:
    def __init__(self):
        print("constructor of employee")

class programmer:
    def __init__(self):
        print("constructor of programmer")

class manager(employee, programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager")

m = manager()
        

#CLASS METHOD
class employuee:
    a=1
    @classmethod #class method na hota to 45 print ho jata 
    def show(self):
     
     print("the class value is:",self.a)
e=employuee()
e.a=45
e.show()


#PROPERTY DECORATER
class employee:
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    # SEETER
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=employee()
e.name="ayush yadav"
print(e.name)



#operater overloading
class number:
    def __init__(self,n):
        self.n=n

    def __add__(self, num):
        return self.n+num.n
n=number(2)
m=number(2)
print(n+m)

