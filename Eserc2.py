import numpy as np
import matplotlib.pyplot as plt

t1 = np.linspace(-0.5, 0.5, 1000)   #intervallo e number of samples (last parameter)
rect = np.where((t1 >= -0.5) & (t1 <= 0.5), 4, 0)

t2C= np.linspace(-1,0,1000)
triC= np.where(t2C,t2C+1,0)

t2D= np.linspace(0,1,1000)
triD= np.where(t2D,1-t2D,0)

tri= np.concatenate([triC,triD])
t2=  np.concatenate([t2C,t2D])

conv= np.convolve(rect, tri, mode="same")
tc= np.linspace(-1.5,1.5, len(conv))

conv2 = np.convolve(rect, rect, mode="same")
tc2 = np.linspace(-1.5, 1.5, len(conv))
rect2 = np.where((tc2 >= -1) & (tc2 <= 1), 4, 0)


#grafico rect
plt.subplot(3,1,1)
plt.grid(True)
plt.stem(t1,rect)
plt.title("rect")
plt.xlabel("Tempo")
plt.ylabel("Ampiezza")
plt.xlim([-5,5])

plt.title("Rect")
plt.xlabel("Tempo")
plt.ylabel("Ampiezza")
plt.xlim([-5,5])

#grafico tri
plt.subplot(3,1,2)
plt.grid(True)
plt.stem(t2,tri)
plt.title("Tri")
plt.xlabel("Tempo")
plt.ylabel("Ampiezza")
plt.xlim([-5,5])

#grafico convoluzione
plt.subplot(3,1,3)
plt.grid(True)
plt.stem(tc,conv)
plt.title("Convoluzione")
plt.xlabel("Tempo")
plt.ylabel("Ampiezza")
plt.xlim([-5,5])

#grafico convoluzione tra rect e se stessa
plt.subplot(3,1,1)
plt.grid(True)
plt.stem(tc2,conv2)
plt.title("Convoluzione 2")
plt.xlabel("Tempo")
plt.ylabel("Ampiezza")
plt.xlim([-5,5])



plt.tight_layout()
plt.show(block=True)
