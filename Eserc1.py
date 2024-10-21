import numpy as np
import matplotlib.pyplot as plt

A =5
T = 2
f = 1
phi = 0

t = np.linspace(0, 2 * T)
signal = A * np.cos((2 * np.pi / T) * t + f)

plt.subplot(2, 1, 1)
#plt.figure(figsize=(6, 5))

plt.xlim(0, 5)
plt.plot(t, signal)
#plt.title('Pippo')
#plt.xlabel('T')
#plt.ylabel('A')


s2 = A * np.cos(((2 * np.pi / T) * t + f)*2)

plt.subplot(2, 1, 2)
plt.xlim(0, 5)
plt.plot(t, s2)

plt.grid(True)
plt.tight_layout()
plt.show(block=True)
