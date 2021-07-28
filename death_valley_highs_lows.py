import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get dates and high temperatures from the file
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
    print(highs)

# plot the high and low temperatures
plt.style.use("seaborn")
fig, ax = plt.subplots()

ax.plot(dates, highs, c = "red", alpha = 0.5)
ax.plot(dates, lows, c = "blue", alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1)

# format the plot
plt.title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize = 20)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperatures (deg F)", fontsize = 16)
plt.tick_params(axis = "both", which = "both", labelsize = 16)

plt.show()
