
# Adapter Pattern
# Converts one interface into another.

class MobileCharger:

    def charge_mobile(self):
        return "Mobile is charging."


class Adapter:

    def __init__(self, charger):
        self.charger = charger

    def charge(self):
        return self.charger.charge_mobile()


charger = MobileCharger()
adapter = Adapter(charger)

print(adapter.charge())