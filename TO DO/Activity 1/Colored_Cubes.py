import matplotlib.pyplot as plt

# TO DO: Apply a color map to your cubes plot.


# The first five cubic numbers
cubes = [1, 8, 27, 64, 125]

plt.style.use('grayscale')
fig, ax = plt.subplots()

ax.plot(cubes, c='red')

ax.set_title("Set of Cubes (first 5)", fontsize=24)
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Values")

ax.tick_params(axis='both', labelsize=14)


# The first 5000 cubic numbers
x = range(1, 5001)
y = [x**3 for x in x]

plt.style.use('grayscale')
fig, ax = plt.subplots()

ax.scatter(x, y, c=y, cmap=plt.cm.inferno, s=10)
# more colors here --> https://matplotlib.org/stable/users/explain/colors/colormaps.html


ax.set_title("Set of Cubes (first 5000)", fontsize=24)
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Values")

ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()