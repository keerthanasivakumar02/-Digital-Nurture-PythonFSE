# Single Responsibility Principle (SRP)
# One class should have only one responsibility.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"


class ReportCard:
    def print_report(self, student):
        print("Student Name:", student.name)
        print("Marks:", student.marks)
        print("Grade:", student.get_grade())


student = Student("Keerthana", 88)
report = ReportCard()
report.print_report(student)