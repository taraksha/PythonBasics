class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(this): #this refers to the current instance of the class. It could be of any name
        return f"{this.name}({this.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Asha", 36)

print(p1.name)
print(p1.age)
p1.myfunc()
print(p1)  # <__main__.Person object at 0x000001C6CC88F940> if __str__ not implemented
p1.age = 63
print(p1)
del p1



#INHERITANCE

class Student(Person):

    def __init__(self, name, age,institution,grade):
        Person.__init__(self, name, age) # same as  super().__init__(name, age)
        self.institution = institution
        self.grade = grade

    def __str__(self):
        return f"{self.name}({self.age}), student at {self.institution} studying Grade {self.grade}"


    def welcome(self):
        print(f"Welcome {self.name} to the Grade {self.grade}")


student = Student('Tanisha',9,"GIIS",4)
student.myfunc()
student.welcome()
print(student)