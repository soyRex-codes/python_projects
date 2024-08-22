#Encapsulation
#Hide internal implementation details from the outside world (abstraction)
#Protect data from external interference or misuse
#Improve code organization and structure
#Encapsulation is a process of binding data and functions into a single unit called class.
#Abstraction: Encapsulation is closely related to abstraction, which is the concept of showing only the necessary information to the outside world while hiding the internal implementation details. By encapsulating the data and methods within a class or object, you can provide a simple interface to interact with the object, while hiding the complexity of the internal implementation.

#US bank structure
"""bank class
1. current balance
2.deposite
3.withdraw
"""

class USBank():
    def __init__(self, name, balance): 
        self.__name=name #private attribute know as Encapsulation for security and easiness
        self.__balance=balance #private attribute
    
    def get__name(self):
        print ("Hello, welcome to Us Bank banking portal")
        return 0
    def get_currentBalance(self):
        return self.__balance #Accessing private attribute
    def deposite(self, deposite):
        if deposite>0 and self.__balance>0:
            self.__balance+=deposite
            return True
        else:
            print("Invalid Amount")
    def withdraw(self, withdraw):
        if withdraw>0 and self.__balance>0:
            self.__balance-=withdraw #Accessing private attribute
            return True
        else:
            print("Invalid Amount")
            
User1=USBank("Tom", 0)
User2=USBank("Jerry", 0)

acc=input("enter you account number: ")
if acc=="101":
    print(User1.name)

elif acc=="102":
    print(User2.name)
    
    
print("select from 1-3, 1.current Balance, 2.Deposite, 3.Withdraw")
x=input("Enter a number: ")
if x=="1":
    print(acc.get_currentBalance)
elif x=="2":
    print(acc.deposite)
elif x=="3":
    print(acc.withdraw)   

"""Encapsulation and Abstraction

You've provided notes on Encapsulation and Abstraction, which are correct. Encapsulation is the process of binding data and functions into a single unit called a class, while Abstraction is the concept of showing only the necessary information to the outside world while hiding the internal implementation details."""        
           