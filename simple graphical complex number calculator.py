#assignemnt08
#Name: Rajkumar Kushwaha
#Built a Complex calculator using built in complex
#CSC130

from tkinter import *
# importing everything from tkinter module
root= Tk()
root.title("complex calculator")
#setting the whole window size i.e giving the dimensions
#for every object on the calculator screen
width=600
height=500
screenwidth=root.winfo_screenwidth()
screenheight=root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=True,height=True)

# Creating the entry fields for complex numbers
# Adding Label
inputtxt = Label(root, text="First Complex:", font=("Arial",14))
inputtxt.grid(row=1,column=1)

#@entry field Firstcomplex realpart

Realpart1 = Entry(root, width=11, font=("Arial", 12))
Realpart1.grid(row = 1, column = 2, padx=10, pady=10)

#@entry field Firstcomplex imaginarypart
Imaginarypart1 = Entry(root, width=11, font=("Arial", 12))
Imaginarypart1.grid(row=1,column=3, padx=10, pady=10)

#Firstcomplex real part
firstlabelreal = Label(root, text="Real Part", width=11, font=("Arial", 12))
firstlabelreal.grid(row = 2, column = 2)
#and imaginary part labels
firstlabelimag = Label(root, text="Imaginary Part", width=11, font=("Arial", 12))
firstlabelimag.grid(row =2, column = 3)

# Second complex
# Adding Label
inputtxt = Label(root, text="Second Complex:", font= ("Arial", 14))
inputtxt.grid(row=3,column=1)

Realpart2 = Entry(root, width=11, font=("Arial", 12))
Realpart2.grid(row=3, column=2, padx=10, pady=10)

Imaginarypart2 = Entry(root, width=11, font=("Arial", 12))
Imaginarypart2.grid(row=3, column=3, padx=10, pady=10)

#secondcomplex real part and imaginary part text labels
firstlabelreal = Label(root, text="Real Part", width=11, font=("Arial", 12))
firstlabelreal.grid(row = 4, column = 2)

#Firstcomplex real part and imaginary part labels
firstlabelreal = Label(root, text="Imaginary Part", width=11, font=("Arial", 12))
firstlabelreal.grid(row = 4, column = 3)

#Result label
inputtxt = Label(root, text="Result:", width=11, font= ("Arial", 14))
inputtxt.grid(row=10,column=1)

#entry field Creating the real result field
result = Entry(root, width=11, font=("Arial", 12))
result.grid(row=10, column= 2, padx=10, pady=10)
#result field for imaginary field
result2 = Entry(root, width=11, font=("Arial", 12))
result2.grid(row=10,column=3, padx=10, pady=10)


#label for real field
firstlabelreal = Label(root, text="Real Part", width=11, font= ("Arial",12))
firstlabelreal.grid(row =11, column = 2)

#label for imaginary field
firstlabelreal = Label(root, text="imaginary Part", width=11, font = ("Arial",12))
firstlabelreal.grid(row =11, column = 3)

#used Built in complex, (can also be done using cplex)
#Creating the function for the operations
def add():
   num1 = complex(int(Realpart1.get()),int(Imaginarypart1.get()))
   #num2 = complex(Imaginarypart1.get())
   num2 = complex(int(Realpart2.get()),int(Imaginarypart2.get()))
   #num4 = complex(Imaginarypart2.get())
   sum=num1+num2
   result.delete(0, END)
   result.insert(END, sum.real)
   result2.delete(0, END)
   result2.insert(END, sum.imag)

def subtract():
   num1 = complex(int(Realpart1.get()),int(Imaginarypart1.get()))
   num2 = complex(int(Realpart2.get()),int(Imaginarypart2.get()))
   
   subtract=num1-num2
   result.delete(0, END)
   result.insert(END,subtract.real)
   result2.delete(0,END)
   result2.insert(END, subtract.imag)

def multiply():
   num1 = complex(int(Realpart1.get()),int(Imaginarypart1.get()))
   num2 = complex(int(Realpart2.get()),int(Imaginarypart2.get()))
   multiply=num1*num2
   result.delete(0, END)
   result.insert(END, multiply.real)
   result2.delete(0,END)
   result2.insert(END, multiply.imag)

def divide():
   num1 = complex(int(Realpart1.get()),int(Imaginarypart1.get()))
   num2 = complex(int(Realpart2.get()),int(Imaginarypart2.get()))
   divide = num1/num2
   result.delete(0, END)
   result.insert(END, divide.real)
   result2.delete(0, END)
   result2.insert(END, divide.imag)



# Create the buttons
addButton = Button(root, text="+", command=add, height=2,width=10)
addButton.grid(row=8, column=2, padx=7)


subtractButton = Button(root, text="-", command=subtract, height=2,width=10)
subtractButton.grid(row=8, column=3, padx=7)

multiplyButton = Button(root, text="*", command=multiply, height=2,width=10)
multiplyButton.grid(row=8, column=4, padx=7)

divideButton = Button(root, text="/", command=divide, height=2,width=10)
divideButton.grid(row=8, column=5, padx=7)

#clearButton = Button(root, text="Clear Entries", command=lambda: Realpart1.delete(0, END) or Imaginarypart1.delete(0, END) or result.delete(0, END) or Realpart2.delete(0,END) or Imaginarypart2.delete(0,END) or result2.delete(0,END), height=2,width=10)
#clearButton.grid(row=12, column=5, padx=10)

firstlabelreal = Label(root, text="Add", width=11, font= ("Arial",12))
firstlabelreal.grid(row =9, column = 2)

firstlabelreal = Label(root, text="Subtract", width=11, font= ("Arial",12))
firstlabelreal.grid(row =9, column = 3)

firstlabelreal = Label(root, text="Multiply", width=11, font= ("Arial",12))
firstlabelreal.grid(row =9, column = 4)

firstlabelreal = Label(root, text="Divide", width=11, font= ("Arial",12))
firstlabelreal.grid(row =9, column = 5)

clearButton = Button(root, text="Clear Entries", command=lambda: Realpart1.delete(0, END) or Imaginarypart1.delete(0, END) or result.delete(0, END) or Realpart2.delete(0,END) or Imaginarypart2.delete(0,END) or result2.delete(0,END), height=3,width=10)
clearButton.grid(row=12, column=5, padx=10)

#label for opertions
inputtxt = Label(root, text="Opertions", font=("Arial",14))
inputtxt.grid(row=8,column=1)

root.mainloop()