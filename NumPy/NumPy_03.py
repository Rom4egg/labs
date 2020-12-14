from matplotlib import pyplot as plt
import matplotlib.animation as anm
import numpy as np 

f = np.genfromtxt("C:/Python_labs/NumPy/Process/Proc.txt", delimiter="\n")

x = np.linspace(0, f.size, f.size, endpoint=True) # ось х

a = [f]

A = np.eye(x.size) - np.roll(np.eye(x.size), -1, axis=1) # делаем матрицу / roll - смещение

for i in range(255):
    a.append(a[i-1]-(0.5*A @ a[i-1])) # считаем уравнение из условия

# графики
fig = plt.figure()
ax = plt.axes(xlim = (0,50), ylim = (0,10))
line, = ax.plot([], [])

# анимация
def init():
    line.set_data(x, a[0])
    return line,

def animate(i):
    y = a[i+1]
    line.set_data(x, a[i])
    return line,

anim = anm.FuncAnimation(fig, animate, init_func=init, frames=256, interval=20, blit=True)

anim.save('proc.gif', writer='imagemagick')
