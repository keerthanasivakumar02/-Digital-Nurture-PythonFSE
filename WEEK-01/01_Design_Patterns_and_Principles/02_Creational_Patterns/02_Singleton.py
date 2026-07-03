# Singleton Pattern
# Ensures that only one object of a class is created.

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Logger object...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        print("Log:", message)


logger1 = Logger()
logger2 = Logger()

logger1.log("Application Started")

print("Both objects are same:", logger1 is logger2)