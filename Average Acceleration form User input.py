#Author= Rajkumar Kushwaha
#writing a program that lets a user to input the initial velocity, final velocity which results the output average accelertaion.
v1,v2,v3= 0,0,0
#Making pattern for the user where they can enter the values they wish
v1= float(input("Enter initial velocity 1:")) #in m/sec
v2= float(input("Enter final velocity 2:"))   #in m/sec
t= float(input("Enter time:"))                #in m/sec
#writing the formula of average accelerataion so that program can calculate the final average acceleration using the assigned values given by the user
a= (v2-v1)/t                               #in m/s^2
#using print statement to print the final average acceleration
print("average acceleation",a,"m/s^2")