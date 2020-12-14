from sympy import Function, Symbol, Eq, dsolve, utilities, sqrt
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

y = Function('y')
x = Symbol('x')

diff = Eq(y(x).diff(x), -2*y(x)) # исходное уравнение
solution = dsolve(diff, y(x)) # решение в sympy
a = solution.subs([(x, 0), (y(0), sqrt(2))]) # частное решение и константа в sympy
diff_solution = solution.subs([(a.rhs, a.lhs)]) # функция решения дифф уравнения


# решение SymPy
x_sym = np.linspace(0, 10) # ось х
diff_function = utilities.lambdify((x,), diff_solution.rhs, modules='numpy') # получаем график уравнения
y_sym = diff_function(x_sym) # для графика

print("Решение SymPy:", diff_solution.rhs)

# решение SciPy
def d_yd_x(y, x):
    return -2*y

y0 = 2**(1/2) # точка по условию
x_sci = np.linspace(0, 10) # ось х
y_sci = odeint(d_yd_x, y0, x_sci) # ось у

# построение графиков
fig, axs = plt.subplots(1,2, figsize = (12,5))
# axs0 - Решение SymPy и SciPy
axs[0].set_title("Решение SymPy и SciPy")
axs[0].plot(x_sym, y_sym, label='SymPy')
axs[0].plot(x_sci, y_sci, '.', label='SciPy', color='red')
axs[0].legend(loc='upper right')
axs[0].grid()
# axs1 - Разность SymPy-SciPy
y_sym = [y_sym[i]-y_sci[i] for i in range(y_sym.size)]
axs[1].plot(x_sym, y_sym)
axs[1].set_title("Разность SymPy-SciPy")
axs[1].grid()

plt.show()