#The code is Python 3 code
import re #re is regular expression moduee imported
import sys #sys module
'''-print a list of token type and its value, in order, of the input tokens
report any lexical error with a proper message such as @unknown'''

#we use the input function to get the file path from the user.
#We then use the open function to read the file

#################################################
#  Tokenize the input string into a list of tokens
#################################################

#################################################
#  Tokenize the input string into a list of tokens
#################################################
#we are using the analysis on the file content
def lexical_analyzer(file):
    #tokens = file.split()
    
    file = re.sub(r'#.*', '', file) #ignore comment
    file = re.sub(r'\s+', ' ', file) #ignore white space
    tokens = re.findall(r'\w+|!=|[^\w\s\!=]|[\(\)\{\}\[\];,\.]+', file) # Split the file content into tokens using regular expressions
    
    keywords = ['if, else', 'while', 'break', 'read', 'write', 'function', 'return']
    
    
    #################################
    ## Check if the token is a keyword and similary for all other below
    ##################################################################
    for token in tokens:
        if token in keywords:
            print('Token:keywords(' + (token) + ')')
        
        elif token == '!=':
            print('Token:NotEqual(!=)')
        
        # Checking if the token is an identifier (using regular expressions), Starts with a letter or an underscore. Followed by zero or more characters that are letters, digits, or underscores.
        elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):
             print('Token:Identifiers(' + (token) + ')')
             
        # Check if the token is an integer (using regular expressions)     
        elif re.match(r'^\d+$', token): #integer
            print('Token:integer(' + (token)+ ')')
            
        # Check if the token is a floating-point number (using regular expressions)    
        elif re.match(r'^\d+\.\d{1,3}$', token): #floating point
            print('Token:floating-point(' + (token) + ')')
 #####################################################################     
 #Various Operators         
        elif token in ['+']:
            print("Token:Addition(+)")
        elif token in ['-']:
            print("Token:Subtraction(-)")
        elif token in ['/']:
            print("Token:Divide(/)")
        elif token in ['*']:
            print("Token:Multiply")
        elif token in ['**']:
            print("Token:Power(**)")
        elif token in ['%']:
            print("Token:remainder or Modulo(%)")    
#############################################################  
#compariosn operators
        elif token in ['<']:
            print ('Token:LThan(<)')
        elif token in ['>']:
            print ('Token:GThan(>)')
        elif token in ['!=']:
            print ('Token:NotEqual(!=)')
        elif token in ['==']:
            print ('Token:Equal(==)')
        elif token in ['>=']:
            print ('Token:GThanEqual(>=)')
        elif token in ['<=']:
            print ('Token:LThanEqual(<=)')                    
################################################################   
         
        elif token in ['=']:
            print ('Token:Assignment Operator(=)')
            
        elif token in ['&']:
            print('Token: and(&)')
        elif token in ['|']:
            print('Token:or(|)')
       
################################################################            
        elif token in ['{']:
            print('Token:Lpar({)')
            
        elif token in ['}']:
            print('Token:Rpar(})')    
            
        elif token in ['(']:
            print('Token: LBrac(()')
        elif token in [')']:
            print('Token: RBrac())')    
            
        elif token in [';']:
            print('Token: Semicolon(;)')
            
        elif token in [',']:
            print['Token: comma(,)']
            

#################################################################################
# File open/read and function execution on it
###################################################################################
file_path = input("Enter the file path: ")
with open(file_path, 'r') as file:
    file_content = file.read() #read and store file in file_content
    lexical_analyzer(file_content) #function call
##################################################################################
#Condition was : must print the output to the output terminal and in a file
#generate a output file of the output result we got in the terminal

# Redirect the output to a file called output.txt
import sys # no one says i can't import something at the middle of the script

with open('output.txt', 'w') as f:
    old_stdout = sys.stdout
    sys.stdout = f
    lexical_analyzer(file_content) 
    sys.stdout = old_stdout
'''This code redirects the standard output to the file output.txt while the program code is executed,
    and then restores the standard output to its original value.'''
#OR

#Run below command in terminal to get the result in a file
#########################################################
#  python lexicalAnalyzer.py > output.txt
##################################################################
#the output.txt file does not need to exist before running the command.
#When you use the > operator to redirect the output to a file, the file will be created automatically if it does not exist.

#to view the file path
import os
print("Output file will be generated at:", os.path.abspath('output.txt'))