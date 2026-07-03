# Command Pattern
# Encapsulates a request as an object.

class Fan:

    def start(self):
        print("Fan Started")


class FanCommand:

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.start()


fan = Fan()
command = FanCommand(fan)

command.execute()