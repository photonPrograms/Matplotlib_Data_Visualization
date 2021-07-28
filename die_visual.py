from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# create a D6
die = Die()

# roll the die
results = []
n = 1000
for i in range(n):
    results.append(die.roll())

# analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequencies.append(results.count(value))

# visualize the results
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency"}
my_layout = Layout(title = f"Results of rolling D6 {n} times", xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename = "d6.html")
