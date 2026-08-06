import qrcode, numpy as np, matplotlib.pyplot as plt
a = np.array(qrcode.make("CLCODING").convert("L"))
y, x = np.where(a == 0)
plt.figure(figsize=(8, 8), facecolor="black")

plt.scatter(
    x + np.random.randn(len(x)) * 2,
    y + np.random.randn(len(y)) * 2,
    c="white",
    s=np.random.randint(1, 15, len(x)),
    alpha=0.7
)
plt.axis("off")
plt.title("Space Dust QR", c="white")
plt.show()