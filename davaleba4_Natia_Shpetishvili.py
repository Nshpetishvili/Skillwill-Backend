class Student:
    university = "Caucasus university" 

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    @property
    def is_passing(self):
        return self.grade > 60

    def increase_grade(self, points):
        self.grade += points


student1 = Student("Natia", 95 , 20)
print(student1)  # Name: Natia, Age: 20, Grade: 95

print(student1.is_passing) 

student1.increase_grade(5) # Name: Natia, Age: 20, Grade: 100
print(student1)