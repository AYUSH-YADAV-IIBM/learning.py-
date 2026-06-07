#instance of class
class employee:
    language="python"
    salary=12000

ayush=employee()
print(f"salary:{ayush.salary},language:{ayush.language} ",)


#self method
class employee:
    language="python"
    salary=2500000
    name="ayush"
    #@staticmethod =ye use karne se self nahi dena parta hain
    def getinfo(self):
        print(f"the name is:{self.name}\nthe language is:\n{self.language}.the salary is:\n{self.salary}")
    def greet(self):
        print("good morning",self.name)
ayush=employee()
ayush.getinfo()
ayush.greet()


#__init__() constructor
class employee:
    @staticmethod
    def greet():
        print("welcome the ayush company to get your info",)


    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language

    def getinfo(self):
        print(f" name is:{self.name}\n salary is:{self.salary}\n language is:{self.language}")

ayush=employee("ayush",500000,"java")
employee.greet()
ayush.getinfo()

rahul=employee("rahul",125000,"python")
employee.greet()
rahul.getinfo()

print("yarly salary ayush:",ayush.salary*12)
print("yarly salary rahul",rahul.salary*12)

if ayush.salary>rahul.salary:
    print(ayush.name,"more salary")

else:
    print(rahul.name,"more salary")

<<<<<<< HEAD
    
=======
    
#q1=create a class "programmer" for storing information of few programmers working microsoft
class programmer:
    company="mocrosoft"
    def __init__(self,name, salary , pin_code):
        self.name=name
        self.salary=salary
        self.pin_code=pin_code

    def getinfo(self):
        print("name is:",self.name)
        print("salary is:",self.salary)
        print("pin_code is::",self.pin_code)
        print("company is:",self.company)

ayush=programmer("ayush",5000000,844111)
ayush.getinfo()
bobby=programmer("bobby",4587700,844112)
bobby.getinfo()




##wap a class "calculater" capable of finding square,squareroot and cube of a number
class square:
    def __init__(self,n):
        self.n=n
    #square
    def square(self):
        print("the square is:",self.n*self.n)
    #cube
    def cube(self):
        print(f"the cube is:{self.n*self.n*self.n}")
    #squareroot
    def squareroot(self):
        print(f"the square root is:{self.n**1/2}")
    
calculeter=square(4)
calculeter.square()
calculeter.cube()
calculeter.squareroot()

#3=creat a class with a class artibutes a; directly usinhg object a=0 does this chnage class artibutes
class demo:
    a=4
o=demo()
print(o.a)# print class artibutes becoz instance artibut is not present
o.a=0 # instance artibutes is set
print(o.a) #print instance artibute becoz instance artibut is present
print(demo.a) # print class artibutes

#4=add a static method in problam to greet the user with hello
class greet:
    @staticmethod
    def greeta():
        print("hello pyare!")
greet.greeta()



#wap in python to class in train which has method to book a ticket.get,status,setno,and fare
import random
class train:
    @staticmethod
    def greet():
        print("welcome to indian railway")
    def __init__(self,TRAINno):
        self.TRAINno=TRAINno
    
    #BOOK TRAIN
    def book(self,fro,to):
        print(f"ticket is booked in train no:{self.TRAINno}\n from:{fro} to:{to}")

    ##runnning status
    def getstatus(self):
        print(f"the train no is :{self.TRAINno} running on time")
    
    ##train fare
    def getfare(self,fro,to):
        print(f"train fare in train no:{self.TRAINno} from:{fro} to:{to} is {random.randint(222,555)}")
t=train(12599)
t.greet()
t.book("patna","hariyana")
t.getfare("patna","hariyana")
t.getstatus()

>>>>>>> e12166d (add)
