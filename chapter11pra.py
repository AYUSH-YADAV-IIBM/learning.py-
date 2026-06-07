#create a class (2-d vacter) and use to create another class representing a 3-d vecter
class twodvecter:
    def __init__(self,n,j):
        self.n=n
        self.j=j
    def show(self):
        print(f"the two d vecter is{self.n}n+ {self.j}j")
class threedvecter(twodvecter):
    def __init__(self, n, j,k):
        super().__init__(n, j)
        self.k=k
    def show(self):
        print(f"the three d vecter is:{self.n}n+ {self.j}j+  {self.k}k")
a=twodvecter(1,2)
a.show()
b=threedvecter(1,2,3)
b.show()