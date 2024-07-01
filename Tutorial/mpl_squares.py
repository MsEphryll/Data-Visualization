import matplotlib.pyplot as plt

squares = [1,4,9,16,26]


# subplots() --> can generate one or more plots in the same figure.
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()