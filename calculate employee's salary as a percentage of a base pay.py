
#writing a programn that reads the numerical codes for each of the four variables as entered by the user
#and lets the user to calculate employee's salary as a percentage of a base pay
#author = Rajkumar Kushwaha
#job class= J, Education= E 
#Merit Rating= M, Self Service= S
J = int(input(" Enter Job Class:"))
E = int(input(" Enter Education:"))
M = int(input("Enter Merit Rating:"))
S = int(input("Years of service:")) 

base = 2000
#percentage base pay = (base + (base * %))''
start_percent=0

if J == 1:
   percentage_base_payj = start_percent
elif J == 2:
   percentage_base_payj = start_percent + 5 
elif J == 3:
   percentage_base_payj = start_percent + 15
elif J == 4:
   percentage_base_payj = start_percent + 50
elif J == 5:
   percentage_base_payj = start_percent + 15
   
if E == 1:
   percentage_base_paye = start_percent
elif E == 2:
   percentage_base_paye = start_percent + 10
elif E == 3:
   percentage_base_paye = start_percent + 25
elif E == 4:
   percentage_base_paye = start_percent + 50
elif E == 5:
   percentage_base_paye = start_percent + 15
   
if M == 0:
   percentage_base_paym = start_percent
elif M == 1:
   percentage_base_paym = start_percent + 10
if M == 2:
   percentage_base_paym = start_percent + 25
   #writing this line 50 to 53 so that User can access the pay base for years above 10
if S <= 10:
   percentage_base_pays = start_percent + 5
if S > 10:
   percentage_base_pays = start_percent+ 4*(S-10)
   #Writing a formula to calculate percentage base pay
   #percentage base pay = PB
sum_of_percent = (percentage_base_payj + percentage_base_paye + percentage_base_paym + percentage_base_pays)/100
salary = base * sum_of_percent + base
    #Using print statement to print the final salary inclduing the percentage base pay
print("employee slaary",salary)
