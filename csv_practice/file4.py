import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print("Gray squirrels: " + str(gray_squirrels_count) + " Cinnamon squirrels: " +
      str(cinnamon_squirrels_count) + " Black squirrels: " + str(black_squirrels_count))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
data_dict_df = pandas.DataFrame(data_dict)
print(data_dict_df)

data_dict_df.to_csv("squirrels_color_count.csv")
