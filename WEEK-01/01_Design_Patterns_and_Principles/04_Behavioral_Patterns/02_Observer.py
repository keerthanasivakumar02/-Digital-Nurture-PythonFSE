# Observer Pattern
# Notifies all registered users when an event occurs.

class Student:

    def update(self, message):
        print("Notification:", message)


class Teacher:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def announce(self, message):
        for student in self.students:
            student.update(message)


student = Student()
teacher = Teacher()

teacher.add_student(student)
teacher.announce("Tomorrow is a holiday.")