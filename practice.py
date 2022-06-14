# OOP practice for Python
import datetime


# Simple class
class Employee:

    num_of_emp = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emp += 1

    # To keep on using email and full name as attributes so that other developers won't have to change their code-
    # -by a method added for this sole purpose or go back to the past codes to fix up the changes in names/emails
    # Java has these built-in, but Python requires it to be built by the developer oneself
    @property
    def email(self):
        return self.first + "." + self.last + "@company.com"

    @property
    def fullname(self):
        return self.first + " " + self.last

    # Setting up the instances to go into fullname property/attribute
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # Deleting an employee's full name
    @fullname.deleter
    def fullname(self):
        print("Deleting name...")
        self.first = None
        self.last = None
        print("Name deleted!")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
        # self or class or instance.variable is important. You cannot access the variable from the same class in Python

    # Class variables and class methods
    # Changes the entirety of a class
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # What if employee details are separated by hyphens instead?
    # Then we must parse it here so that it is easier to input data
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # Some common special methods that are quite essential for any projects for debugging and unambiguity
    # Special methods change how objects are displayed, and you can also make normal functions-
    # -available to be used by objects by making them special methods
    # You can customise how objects compare to each other and check for equalities, and add or subtract, etc.
    # Unless you're dealing with very complicated projects, __init__ and the below two should be enough
    # They can also be called "dunders", because of its Double UNDERScores
    # check https://docs.python.org/3/reference/datamodel.html#special-method-names for further details
    # Same as calling repr(object) and str(object) on their own
    # __repr__ is meant to be seen by other developers for debugging with unambiguity
    # __str__ is meant to be seen by the end user for reading
    # __repr__ is good to have as a minimum, as when a user calls __str__, __repr__ will be called at least
    # __init__ is also a special method
    # Check their examples and results in the terminal below
    def __repr__(self):
        return self.fullname

    def __str__(self):
        return self.fullname + " " + self.email + " " + str(self.pay)


# Using an inheritance class as Developers also have names, emails and pays
class Developer(Employee):

    raise_amount = 1.10
    # Developers get more pay rise compared to Employees!

    def __init__(self, first, last, pay, prog_lang):
        # super().__init__(first, last, pay) method is essentially the same as:
        # Employee.__init__(self, first, last, pay) for calling the parent classes
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# Another inheritance class for Managers
class Manager(Employee):

    raise_amount = 1.15
    # Managers get even more pay rise than Developers!

    # employees=None will be used for appending the list of employees that they manage
    # It is usually a good idea to just set it as none, as putting in mutable data types-
    # -such as lists or dictionaries in default arguments are not recommended
    def __init__(self, first, last, pay, employees=None):
        # super().__init__(first, last, pay) method is essentially the same as:
        # Employee.__init__(self, first, last, pay) for calling the parent classes
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # Just some simple methods from here on
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("Manages:", emp.fullname)


emp_1 = Employee("John", "Smith", 100_000)
emp_2 = Employee("John", "Doe", 120_000)

dev_1 = Developer("Smith", "Developer", 120_000, "Python")
dev_2 = Developer("Doe", "Developer", 140_000, "Java")

mgr_1 = Manager("Jono", "Smith", 150_000, [dev_1])
mgr_2 = Manager("Jose", "Smith", 180_000, [dev_2])

Employee.set_raise_amount(1.06)
# Essentially the same as Employee.raise_amount = 1.06
# But using a class method to do that instead

emp_str_1 = "Johnny-Smith-110_000"
emp_str_2 = "Johnny-Doe-130_000"

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

# Monday
my_date_true = datetime.date(2016, 7, 11)
# Sunday
my_date_false = datetime.date(2016, 7, 10)

print("Employee: " + emp_1.fullname, emp_1.email, emp_1.pay, emp_1.apply_raise())
print("Employee: " + emp_2.fullname, emp_2.email, emp_2.pay, emp_2.apply_raise())
print("Developer: " + dev_1.fullname, dev_1.email, dev_1.pay, dev_1.apply_raise(), dev_1.prog_lang)
print("Developer: " + dev_2.fullname, dev_2.email, dev_2.pay, dev_2.apply_raise(), dev_2.prog_lang)
print("Manager: " + mgr_1.fullname, mgr_1.email, mgr_1.pay, mgr_1.apply_raise())
mgr_1.print_emp()
print("Manager: " + mgr_2.fullname, mgr_2.email, mgr_2.pay, mgr_2.apply_raise())
mgr_2.print_emp()
print("New Employee: " + new_emp_1.fullname, new_emp_1.email, new_emp_1.pay, new_emp_1.apply_raise())
print("New Employee: " + new_emp_2.fullname, new_emp_2.email, new_emp_2.pay, new_emp_2.apply_raise())
print("The number of employees: " + str(Employee.num_of_emp))
print("Is it workday? " + str(Employee.is_workday(my_date_true)))
print("Is it workday? " + str(Employee.is_workday(my_date_false)))
# print(help(Developer))

# Some notes when experimenting with inheritances
# isinstace() tells us if an object is an instance of a class
# issubclass() tells us if a class is a subclass of a class
# Such as:
print("Is Manager an instance of Employee? " + str(isinstance(mgr_1, Employee)))
# Will be true as manager is an instance of Employee
print("Is Manager an instance of Developer? " + str(isinstance(mgr_1, Developer)))
# However, won't be true as Manager is not an instance of Developer
# Although they both come from Employee, their inheritances are separate
# And with the same logic, the below examples should make their own sense
print("Is Developer a subclass of Employee? " + str(issubclass(Developer, Employee)))
print("Is Employee a subclass of Manager? " + str(issubclass(Manager, Employee)))
print("Is Manager a subclass of Developer? " + str(issubclass(Manager, Developer)))

# Printing the special methods and examples
# There is no more unambiguity from printing objects by itself
# __str__ gets used first
print("Called object emp_1 itself: <__main__.Employee object at 0x102fe1600>")
print("Called object emp_2 itself: <__main__.Employee object at 0x102fe1540>")
# If you want to call __repr__ or __str__ separately:
print("Called object emp_1 using __repr__: " + emp_1.__repr__())
print("Called object emp_2 using __str__: " + emp_2.__str__())

# Checking the property, setter and getter methods
emp_1.fullname = "Name Change"
print("First: " + emp_1.first)
print("Last: " + emp_1.last)
print("Full: " + emp_1.fullname)
print("Email: " + emp_1.email)
del emp_1.fullname
# To check if the name is deleted, uncomment the line of code below and check for a typeerror during initialisation
# print(emp_1)

# Inheritance is extremely important for any mid-to-big-sized projects
# Try to utilise them as much as possible
