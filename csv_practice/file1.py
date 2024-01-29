import csv


with open("weather_data.csv", 'r') as data_file:
    data = data_file.readlines()
    print(data)


with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        try:
            temperatures.append(int(row[1]))
        except Exception:
            pass
        print(row)

    print(temperatures)
