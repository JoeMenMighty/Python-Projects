'''
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
'''

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

age = int(age)

days_90 = 90 * 365
weeks_90 = 90 * 52
months_90 = 90 * 12


days_left = days_90 - (age * 365)
weeks_left = weeks_90 - (age * 52)
months_left = months_90 - (age * 12)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")