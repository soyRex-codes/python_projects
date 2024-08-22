# Author=Rajkumar Kushwaha
# writing a program that can prompt a user to enter the maximum degree of polynomial,
#coefficients of polynomial as well as the value of x.
#then it will be invoking the function and printing the indicated output based on the data given by the user.def Poly(l1,x):
def Poly(l1,x):
          # l1 is the list of coefficients of polynomials
          # x is the value of x we need to find the value of p(x)
          pow=0 # pow is the variable to have power count
          val=0 # value is the final p(x) we need to calculate 
          #using for loop for calculation of polynomial
          for i in l1:
                 val=val+(i)*((x)**pow) 
                 pow+=1 # increment of the power value
          return val # it returns the final p(x) value
#using input to prmopt the user to enter the maximum degree of the function.
max_degree=int(input("Enter the maximum degree of the function:"))
# using coeff=[] to get the list of coffecient
coeff=[]
for j in range(0,max_degree+1):
    c=int(input(f"Enter the coefficient of x^{j}: "))
    coeff.append(c)
x=int(input("Enter the value of x:"))
#using print statement to print the indicated output value of the polynomial at x
print("The value of the polynomial at x=",x ,"is: ",Poly(coeff,x))