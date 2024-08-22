#1.class, create an object, instance for that class
class superhero():
    def __init__(self,name, height, race, type, Superpower, speed):
        self.__name=name
        self.__height=height
        self.__race=race
        self.__type=type
        self.__Superpower=Superpower
        self.__speed=speed
        #method/function of the class
    def superpower(self, strength):
        print(f" My super power is {strength}")
#1.2 object from class
superhero1=superhero("superman", 6.4, "asian", "aggresive", "flying", 220)
superhero1.superpower("breath in outer space is")
superhero2=superhero("rustam", 5.7,"middle-east", "kind","converts water to rose water","500B in2sec")
superhero1.superpower("waterskii")

#instance
print(superhero1.name)
print(superhero2.type)


""""-------------------------------------------------------------
-------------------------------------------------------------"""
#inheritance(child of parent clas)
# =>from that class(subclass), creating subclass from a class in called inheritance
""""-------------------------------------------------------------
-------------------------------------------------------------"""
class Ironman(superhero):
    def __init__(self,name, height, race, type, Superpower, speed, realname, power, GF):
        super().__init__(name, height, race, type, Superpower, speed) #call the constructor
        self.__realname=realname
        self.__power=power
        self.__GF=GF
    def superpower(self, strength): #override the function/method of parent class
        print("suuUUUU")
    
     #we can add new methods to child class
    def favouritefood(self, favfod):
        print(f"my favourite food is {favfod}")   
    
#polymorphism(shapeshifter)
"""Polymorphism is the ability of an object to take on multiple forms. In other words, an object
of a particular class can behave like an object of a different class. This is achieved through
method overriding or method overloading."""
#overiding is fun because we can use same name for multiple functions
#and overwrite their parameters to use functions differently



"""Encapsulation: Learn how to use encapsulation to hide internal implementation details of your classes and
make them more modular and reusable.


""""""Composition: Understand how to use composition to create objects from other objects, which will help you design more complex systems.
Error Handling: Learn how to use try-except blocks to handle errors and exceptions in your code, making it more robust and reliable.
File Input/Output: Understand how to read and write files, which will help you work with data storage and retrieval.
Data Structures: Learn about other data structures like lists, dictionaries, sets, and tuples, which will help you work with different types of data.
Algorithms: Study algorithms like sorting, searching, and graph traversal, which will help you solve complex problems efficiently.
Object-Oriented Design: Learn how to design classes and objects that follow the principles of object-oriented programming, making your code more maintainable and scalable.
Practice: Practice, practice, practice! Work on projects that challenge you to apply what you've learned. This will help you solidify your understanding of classes and other Python concepts.
"""
