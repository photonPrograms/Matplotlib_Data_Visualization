import matplotlib.pyplot as plt

plt.style.use("seaborn")
fig, ax = plt.subplots()

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Greens, s = 10)

# set the chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)


# set size of tick labels
ax.tick_params(axis = "both", which = "major", labelsize = 14)

# set the range for axes
ax.axis([0, 1100, 0, 1100000])

#plt.show()
# saving the file instead of 'showing'
plt.savefig("squares_plot.jpeg", bbox_inches = "tight")
