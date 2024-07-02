import matplotlib.pyplot as plt

x = range(1, 1001)
y = [i**2 for i in x]

plt.style.use('default')
fig, ax = plt.subplots()

# color part 1
# ax.scatter(x, y, c='black', s=40) # c --> for color (could be RGB(0, 0.9, 8))

# color part 2
ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=10)
# cmap --> for color map
# pass the list of y-values to c, and then tell pyplot which colormap to use the 
# cmap argument. This colors the points with lower y-values light blue and higher 
# y-values dark blue.


# Set chart name and label axes.
ax.set_title("Square Numbers (single point) with loop")
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

# major -->  might appear at every integer (0, 1, 2, ... )
# minor --> might appear at every half integer (0.5, 1.5, 2.5, ...)

ax.axis([0, 1100, 0, 1100000])

plt.show()

# if you want to automatically save the plot file, replace plt.show() to plt.savefig()
# plt.savefig('square_plot.png', bbox_inches='tight') --> sample