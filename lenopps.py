class items:
    def __init__(self,items):
        self.items=items
    
    def __len__(self):
        return len(self.items) ## len method usi tra use hota hain

i=items(["apple","banana","kela"])
print(len(i))