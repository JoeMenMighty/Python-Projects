sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Copy and Paste your code below this line 👇
all_words = sentence.split()
result = {word:len(word) for word in all_words}
# Then click "Run" to execute the tests

print(result)