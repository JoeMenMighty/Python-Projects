with open('file1.txt') as file_1:
    file_1_list = file_1.readlines()
    file_1_list = [num.strip('\n') for num in file_1_list]

with open('file2.txt') as file_2:
    file_2_list = file_2.readlines()
    file_2_list = [num.strip('\n') for num in file_2_list]

result = [int(number) for number in file_1_list if (number in file_2_list)]
# First *fork* your copy.
# Copy and Paste your code above this line 👆
# Then click "Run" to execute the tests


print(result)
