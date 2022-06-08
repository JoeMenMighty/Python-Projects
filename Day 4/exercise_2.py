'''
You are going to write a program which will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. 
For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
'''
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#get the number of people availlable
total_mem = len(names)

#generate a random number in the range of the people available
choice = random.randint(0, total_mem-1)

#select person based on the number generated
choice_person = names[choice]
print(f"{choice_person} is going to buy the meal today!")