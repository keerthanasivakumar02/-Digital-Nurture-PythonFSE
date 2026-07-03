# Liskov Substitution Principle (LSP)

class Employee:
    def work(self):
        print("Employee is working.")


class Developer(Employee):
    def work(self):
        print("Developer is writing code.")


class Tester(Employee):
    def work(self):
        print("Tester is testing the software.")


employees = [Developer(), Tester()]

for emp in employees:
    emp.work()