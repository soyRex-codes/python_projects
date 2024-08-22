#classes in python
class fan(): #super class
    def __init__(self, brand, speed, quality):
     self.brand=brand
     self.speed=speed
     self.quality=quality
    #
# you need to define def color , inside the fan class.
#methods/functions/extra features for our object
    def color(self, color_type):
        print(f"fan color is {color_type}")

#creating object for class
fan1=fan("philpis",220, "5/10")
fan1.color("red")
fan2=fan("samsung",330, "9/10")
fan2.color("blue")
#alright we created our object using class and method, that's all

#we can use the object now and its methods  
fan1.color() #instance of a class

