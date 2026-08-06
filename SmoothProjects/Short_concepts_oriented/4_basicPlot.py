import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(
    x, y,
    linestyle="--",
    color="red"
)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph")
plt.grid(True)
plt.show()