class SoftwareDeveloper(object):

    # class attribute
    alias = "keyboard magician"
    
    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        self.on = False

# instance
enginer1 = SoftwareDeveloper("Kenwood", 22, "Junior developer", 5000)
print(enginer1.name, enginer1.age, enginer1.level)
print(SoftwareDeveloper.alias)

enginer2 = SoftwareDeveloper("Madaline", 20, "Senior developer", 7000)
print(SoftwareDeveloper.alias)

print(enginer1.on)
print(enginer1.on)


# recap
""" Class: template for creating objects.
A class is the blueprint of oopp. 
Objects created using the same class will
possess the same characteristics.
An Object is an instance of a class.
instance attributes: defined in __init__(self)
To Instantiate means to create an instance of a class
A Method is a function defined in a class.
Attribute a variable bound to an instance of a class/ 
"""