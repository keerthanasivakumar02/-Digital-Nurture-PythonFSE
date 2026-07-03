# Proxy Pattern
# Controls access to another object.

class StudentRecord:

    def view(self):
        print("Displaying student record.")


class StudentProxy:

    def __init__(self):
        self.record = StudentRecord()

    def view(self):
        print("Checking permission...")
        self.record.view()


proxy = StudentProxy()
proxy.view()