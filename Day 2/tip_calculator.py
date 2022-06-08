'''
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

'''

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#Welcome message
print("Welcome to Mighty's tip calculator")

#ask user for total bill
total_bill = float(input("What was the total bill: $"))

#ask user for percentage
bill_percent = int(input("What percentage tip will you like to give? 10, 12, 15?: "))

#convert percentage to odd multiplier
bill_mult = (1+(bill_percent/100))

#ask for number of people
num_people = int(input("How many people will split the bill?: "))

#calculate each person bill
bill_each = (total_bill * bill_mult)/num_people

#round up bill to 2 dec.
bill_each_round = round(bill_each, 2)

#store and display message for bill
message = f"Each person will pay: ${bill_each_round}"
print(message)