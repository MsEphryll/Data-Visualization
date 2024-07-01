import matplotlib.pyplot as plt

# TO DO: A number of raised to the third power is a cube. Plot the first five 
# cubic numbers and then the first 5000 cubic numbers.

# The first five cubic numbers
cubes = [1, 8, 27, 64, 125]

plt.style.use('grayscale')
fig, ax = plt.subplots()

ax.plot(cubes)

ax.set_title("Set of Cubes (first 5)", fontsize=24)
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Values")

ax.tick_params(axis='both', labelsize=14)


# The first 5000 cubic numbers
x = range(1, 5001)
y = [x**3 for x in x]

plt.style.use('grayscale')
fig, ax = plt.subplots()

ax.scatter(x, y, s=10)

ax.set_title("Set of Cubes (first 5000)", fontsize=24)
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Values")

ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()