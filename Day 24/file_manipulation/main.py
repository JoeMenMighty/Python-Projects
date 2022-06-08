# read a file
with open('my_file.txt') as file:
    contents = file.read()
    print(contents)

# write into a file. will create a new file if the file to write to does not exist
with open('new_file.txt', mode='w') as file2:
    file2.write('Here is a new file.')

# add to a file
with open('my_file.txt', mode='a') as file3:
    file3.write('\nA new line created')

# using file paths
with open('/home/student/Desktop/desktop_file.txt', mode='w') as file4:
    file4.write('\nThis is a new line in the Desktop File.')


