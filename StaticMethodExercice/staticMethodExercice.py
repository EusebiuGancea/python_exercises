# static methods = a method that belong to a class rather than any
#object from that class. Usually used for general utility functions

# Instance methods = best for operations on instances of the class (objects)
# Static methods = best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugen", "Manager")
employee2 = Employee("Ion", "Cook")

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
