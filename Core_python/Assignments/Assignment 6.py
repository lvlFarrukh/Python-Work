# Question N0 1

# Object Oriented Programming:
#     Object-oriented programming is a programming paradigm based on the concept of "objects",
#      which can contain data, in the form of fields, and code, in the form of procedures.
#       A feature of objects is an object's procedures that can access and often modify the 
#       data fields of the object with which they are associated.


# Question N0 2

# Advantages of OOP:

#   -> It provides a clear modular structure for programs which makes it good for defining
#      abstract datatypes in which implementation details are hidden.
#   -> Objects can also be reused within an across applications. The reuse of software also 
#      lowers the cost of development. More effort is put into the object-oriented analysis and 
#      design, which lowers the overall cost of development.
#   -> It makes software easier to maintain. Since the design is modular, part of the system 
#      can be updated in case of issues without a need to make large-scale changes.


# Question N0 3

            # Function                         |                 Method
# ----------------------------------------------------------------------------------------------

# 1) Function are use in anywhere program.     |  1) Method are use in the class body.

# 2) It is call after the body of the          |  2) Method is use by using object reference.
#    function by its name.

# ---------------------------------------------------------------------------------------------- 


# Question N0 4:

# CLASS:
#       class is a blueprint for creating objects (a particular data structure), providing 
#       initial values for state (member variables or attributes), and implementations of
#       behavior (member functions or methods).

# OBJECT:
#       In object-oriented programming (OOP), objects are the things you think about first 
#       in designing a program and they are also the units of code that are eventually derived 
#       from the process. Each object is an instance of a particular class or subclass with the 
#       class's own methods or procedures and data variables.

# ATTRIBUTE:
#       In Object-oriented programming(OOP), classes and objects have attributes. Attributes 
#       are data stored inside a class or instance and represent the state or quality of the 
#       class or instance. In short, attributes store information about the instance.

# BEHAVIOUR:
#       A class's behavior determines how an instance of that class operates; for example, how it 
#       will "react" if asked to do something by another class or object or if its internal state 
#       changes. Behavior is the only way objects can do anything to themselves or have anything
#       done to them.

    

# Question N0 5:

class Car:
    number_of_car = 0
    def __init__(self, model, color, name, horsepower, milage):
        self.model = model
        self.color = color
        self.name = name
        self.horsepower = horsepower
        self.milage = milage
        Car.number_of_car += 1
    
    def display_detail(self):
        print(f"Car name: {self.name}\nModel: {self.model}\nColor: {self.color}\nHorsepower: {self.horsepower}\nMilage: {self.milage}")
    
    def update_milage(self, milage):
        self.milage = milage
        
    def display_all_cars(self):
        print(f"Total object are: {Car.number_of_car}")
        
        
civic1 = Car('2018', 'Black', 'Civic Turbo', '1800 cc', '50 km')
civic2 = Car('2015', 'white', 'Civic Tr', '1800 cc', '50 km')
civic3 = Car('2012', 'Black', 'Civic ', '1800 cc', '50 km')
civic4 = Car('2016', 'white_gray', 'Civic Turbo', '1800 cc', '50 km')
civic5 = Car('2012', 'Black', 'Civic', '1800 cc', '50 km')

civic.update_milage('100km')
civic. display_detail()
civic.display_all_cars()
