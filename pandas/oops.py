class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("Welcome, ", self.name)

    def getMarks(self):
        print(f"Dear {self.name}, You have got {self.marks} marks!")

s1 = Student("karan", 56)
s2 = Student("arjun", 34)
s1.welcome()
s2.getMarks()