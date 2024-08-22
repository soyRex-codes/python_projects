class myclass():
    def __init__(self, name, age):
        self.name=name
        self.age=age
        #method/extra features
    def mymethod(self, sem):
        print(f"sup{sem}")
            
#object
class1=myclass("A",51)
class2=myclass("B",55)

#accesing instance variable
print(class1.name)
class1.mymethod("fall")
print(class2.age)

#inheritance            
class subclass(myclass):
    def __init__(self, name, age, gender):
        super(). __init__(self, name, age)
        self.gender=gender
    def nationality(self, nationality):
        print(f"sup bro{nationality}")
        
#creating an instance of subclass
#subclass object
subclass_instance=subclass("rex", 53, "M")
print(subclass_instance.gender)
subclass_instance.nationality("Mexican")
 #-----------------------------------------------------------------------
 #--------------------------------------------------------------------------         
#polymorphism(shapeshifter) or (Greek word that means "many forms)
"""Polymorphism is the ability of an object to take on multiple forms. In other words, an object
of a particular class can behave like an object of a different class. This is achieved through
method overriding or method overloading.

Method overloading is a type of polymorphism where multiple methods with the same
name can be defined, but with different parameter lists. This allows us to perform
different actions based on the input parameters."""
#example
class Animal():
    def __init__(self):
        print("The animal make  a sound")
        
class Dog(Animal):
    def sound(self):
        print("The dog barks")
class cat(Animal):
    def sound(self):
        print("The cat meows.")

dog1=Dog()
cat1=cat()

dog1.sound()  # Output: The dog barks.
cat1.sound()  # Output: The cat meows.

#overiding is fun because we can use same name for multiple functions
#and overwrite their parameters to use functions differently