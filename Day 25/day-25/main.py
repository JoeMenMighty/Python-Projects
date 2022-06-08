# # with open('weather_data.csv') as file:
# #     data = file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     all_temps = []
# #     for row in data:
# #         new_temp = row[1]
# #         all_temps.append(new_temp)
# #
# #     for temp in all_temps[1:]:
# #         temperatures.append(int(temp))
#
# import pandas
# # data = pandas.read_csv('weather_data.csv')
# # # print(data)
# #
# # # changing dataframe to a dictionary
# # data_dict = data.to_dict()
# #
# # # changing a  row to  list
# # # temp_list = data['temp'].to_list()
# # #
# # # # average temperature
# # # print(data['temp'].mean())
# # # print(data['temp'].max())
# # #
# # # # pull out a row
# # # print(data[data.temp == data.temp.max()])
# # # # print(temp_list)
# #
# # # convert monday' temp to farhenheiht
# # monday_temp_farenheit = data[data.day == 'Monday'].temp * 1.8 + 32
# # print(monday_temp_farenheit)
# #
# # new_dict = {
# #     'Names': ['Ama', 'Kofi', 'Jamal'],
# #     'Scores': [12, 34, 76]
# # }
# # data2 = pandas.DataFrame(new_dict)
# # data2.to_csv('new_csv.csv')
#
#  # Technique one
# data = pandas.read_csv('Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# black_count = 0
# cinnamon_count = 0
# gray_count = 0
#
# for val in data['Primary Fur Color']:
#     if val == 'Black':
#         black_count += 1
#     elif val == 'Cinnamon':
#         cinnamon_count += 1
#     elif val == 'Gray':
#         gray_count += 1
#
# dict_colors = {
#     'Colors' : ['Black', 'Cinnamon', 'Gray'],
#     'Count' : [black_count, cinnamon_count, gray_count],
# }
# fur_colors_df = pandas.DataFrame(dict_colors)
# fur_colors_df.to_csv('fur_colors.csv')
#
#
# # technique 2 to count
# black_counter = len(data[data['Primary Fur Color'] == 'Black'])
# cinnamon_counter = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# gray_counter = len(data[data['Primary Fur Color'] == 'Gray'])


# # reading files using file opener
# with open('weather_data.csv') as data_file:
#     weather_data = data_file.readlines()
#     print(weather_data)


# # using the csv module
# import csv
#
# with open('weather_data.csv') as data_file:
#     weather_data = csv.reader(data_file)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != 'temp':
#             temp = int(row[1])
#             temperatures.append(temp)
#
#     print(temperatures)

# # using the pandas library
# import pandas
#
# data_file = pandas.read_csv('weather_data.csv')
# print(data_file['temp'].mean(), data_file['temp'].max())
# print(data_file[data_file.temp == data_file.temp.max()])
# convert = int(data_file[data_file.day == 'Monday'].temp) * 1.8 + 32
# print(convert)


# creating new csv file
import pandas

data_file = pandas.read_csv('Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
black_sq = len(data_file[data_file['Primary Fur Color'] == 'Black'])
gray_sq = len(data_file[data_file['Primary Fur Color'] == 'Gray'])
cinnamon_sq = len(data_file[data_file['Primary Fur Color'] == 'Cinnamon'])

new_fur_dict = {
    'Primary Fur Colors': ['Black', 'Cinnamon', 'Gray'],
    'Count of color': [black_sq, cinnamon_sq, gray_sq]
}
new_fur_df = pandas.DataFrame(new_fur_dict)
new_fur_df.to_csv('new_fur_file.csv')

