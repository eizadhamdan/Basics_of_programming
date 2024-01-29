import pandas


data = pandas.read_csv("weather_data.csv")

print(data)
print(data["temp"])
print(type(data["temp"]))
print(type(data))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# Average temperature
print(sum(temp_list) / len(temp_list))
print(data["temp"].mean())

# Max temperature
print(data["temp"].max())

# get data in columns
print(data.condition)
print(data.temp)

# get data in row
print(data[data.day == "Monday"])           # this returns a row

monday = data[data.day == "Monday"]
print(monday.condition)
