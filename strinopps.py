class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def __str__(self):
        return f"student name is:{self.name}\nstudent roll number is:{self.roll}"
student=student("ayush",157)
print(student)