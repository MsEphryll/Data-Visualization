# importing pyplot module using plt as its alias.
# pyplot module --> contains a number of functions that generate charts and plots.
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1,4,9,16,26]


# subplots() --> can generate one or more plots in the same figure.
# fig --> represents the entire figure or collection of plots that are generated.
# ax --> represents the individual plot or subplots. Most used variable ta oll times.
plt.style.use('ggplot')
fig, ax = plt.subplots()

# linewidth --> controls the thickness of the line that plot() generates.
ax.plot(input_values, squares, linewidth=3)


# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)  # sets a title for the chart

# allows to set title for each axes
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14) # styles the tick marks


# open's Matplotlibb viewer and displays the plot
plt.show()