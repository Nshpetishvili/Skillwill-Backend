class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class PersonAttributeMixin:
    @property
    def formatted_attributes(self):
        attributes = [f"{attr}: {getattr(self, attr)}" for attr in self.__dict__]
        return ", ".join(attributes)

class Student(Person, PersonAttributeMixin):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university

student = Student("Natia", "Shpetishvili", 20, "Caucasus University")
print(student.formatted_attributes)
