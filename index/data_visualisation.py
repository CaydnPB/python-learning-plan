import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
siny = np.sin(x)
cosy = np.cos(x)
tany = np.tan(x)

plt.plot(x, siny, label="Sin Function")
plt.plot(x, cosy, label="Cos Function")
plt.plot(x, tany, label="Tan Function")

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Trigonometric Functions")

plt.legend()

plt.show()