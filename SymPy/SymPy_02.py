from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt

with open("SymPy/large.txt", 'r') as f:
    size = int(f.readline()) # размерность вектора неизвестных
    A1 = np.loadtxt("SymPy/large.txt", skiprows=1) 
# матрица А
A = A1[:size]
# вектор b
b = A1[size]

# решение уравнения
ans = linalg.solve(A,b)

# построение графика
x = np.linspace(0, size, size)
plt.bar(x, ans)
plt.grid()

plt.show()