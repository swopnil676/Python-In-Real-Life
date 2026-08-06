import numpy as np
import matplotlib.pyplot as plt

x, y = np.linspace(-2, 1, 1000), np.linspace(-1.5, 1.5, 1000)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y
Z = np.zeros_like(C)
img = np.zeros(C.shape)

for i in range(50):
    Z = Z**2 + C
    img += (abs(Z) < 2)

plt.imshow(img, extent=(-2, 1, -1.5, 1.5), cmap='inferno')
plt.title("Mandelbrot Fractal")
plt.axis('off')
plt.show()