# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data['tempf']))

data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
#
# print(sum(temp_list) / len(temp_list))


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit


tuesday = data[data.day == "Tuesday"]
monday_temp = tuesday.temp[0]
print(monday_temp)

# data_squirrels = pandas.read_csv("squirrels.csv")
#
# fur = data_squirrels["Primary Fur Color"].value_counts()
#
# squirrels_count = {
#     "Fur color": ["Gray", "Cinnamon", "Black"],
#     "Count": [fur.Gray, fur.Cinnamon, fur.Black]
# }
#
# squirrels_count_df = pandas.DataFrame(squirrels_count)
# squirrels_count_df.to_csv("squirrels_count.csv")
