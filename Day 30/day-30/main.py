try:
    file = open('new1.txt', mode='r')
    new_dict = {'key': 'value'}
    print(new_dict['key'])
except FileNotFoundError as error_msg:
    # file = open('new.txt', mode='w')
    # file.write('This is a new file created')
    print(f"{error_msg} cannot be found. New one created")
except KeyError as error_msg:
    print(f'{error_msg}')
else:
    # content = file.read()
    # print(content)
    print('try did not work')
finally:
    pass
    # file.close()
