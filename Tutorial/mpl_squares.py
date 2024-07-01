# importing pyplot module using plt as its alias.
# pyplot module --> contains a number of functions that generate charts and plots.
import matplotlib.pyplot as plt

squares = [1,4,9,16,26]


# subplots() --> can generate one or more plots in the same figure.
# fig --> represents the entire figure or collection of plots that are generated.
# ax --> represents the individual plot or subplots. Most used variable ta oll times.
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)


# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)


# open's Matplotlibb viewer and displays the plot
plt.show()