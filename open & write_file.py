#To read from a file in Python, you can use the open() function
#to open the file in read mode ('r'). The open() function returns a file object.

#read a file: 
with open("testfile.txt", 'r') as file:
    content=file.read()
    print(content)
    
#write to File    
with open("testfile.txt", 'w') as file:
    file.write("This is a test write in a file in python\n")
    file.write("also, I am Raj, the writer btw :\n")
    