class Person:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name

    def display_details(self):
        return f"Student ID: {self.__student_id}, Name: {self.__name}"

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name


class Student:
    def __init__(self, student_id, name):
        self.__person = Person(student_id, name)
        self.__grades = {}

    def add_grade(self, subject, grade):
        self.__grades[subject] = grade

    def average_grade(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def display_details(self):
        return self.__person.display_details() + f", Average Grade: {self.average_grade()}"


class StudentManagementSystem:
    def __init__(self):
        self.__students = {}

    def add_student(self, student_id, name):
        student = Student(student_id, name)
        self.__students[student_id] = student

    def show_student_details(self, student_id):
        if student_id in self.__students:
            return self.__students[student_id].display_details()
        return "Student not found."

    def show_student_average_grade(self, student_id):
        if student_id in self.__students:
            return f"Student ID: {student_id}, Average Grade: {self.__students[student_id].average_grade()}"
        return "Student not found."


sms = StudentManagementSystem()

sms.add_student(1, "Natia")
sms.add_student(2, "Vasiko")

alice = sms._StudentManagementSystem__students[1]
alice.add_grade("Math", 90)
alice.add_grade("Science", 85)

print(sms.show_student_details(1))
print(sms.show_student_details(3))
print(sms.show_student_average_grade(1))
