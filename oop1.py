se1 = ["Software engineer", "Amanda", 20, "Intern Developer", 1000]
se2 = ["Software engineer", "Amanda", 20, "Intern Developer", 1000]
de1 = ["Designer", "Philip"]

# class
class SoftwareEngineer(object):

    # class attribute
    alias = "keyboard magician"
    
    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        self.on = False

    # instance method
    def code(self):
        print(f"{self} is writing code ...")

se1 = SoftwareEngineer("Bella", 21, "Intermediate", 3000)
