from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# create 2 D6
die_1 = Die()
die_2 = Die()

# roll the die
results = []
n = 1000
for i in range(n):
    results.append(die_1.roll() + die_2.roll())

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequencies.append(results.count(value))

# visualize the results
x_values = list(range(2, max_result + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency"}
my_layout = Layout(title = f"Results of rolling 2 D6 {n} times", xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename = "d6_2.html")
