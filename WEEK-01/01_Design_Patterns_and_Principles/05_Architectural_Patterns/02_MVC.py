# Model-View-Controller (MVC) Pattern

# Model
class Employee:

    def __init__(self, name):
        self.name = name


# View
class EmployeeView:

    def show(self, employee):
        print("Employee Name:", employee.name)


# Controller
class EmployeeController:

    def __init__(self, employee, view):
        self.employee = employee
        self.view = view

    def display_employee(self):
        self.view.show(self.employee)


employee = Employee("Keerthana")
view = EmployeeView()
controller = EmployeeController(employee, view)

controller.display_employee()