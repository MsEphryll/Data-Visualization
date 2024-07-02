import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 2]

plt.style.use('grayscale')
fig, ax = plt.subplots()

# to plot a single point
ax.scatter(x, y, s=50) # s --> size of the point set to 50

# Set chart name and label axes.
ax.set_title("Square Numbers (single point)")
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()