import numpy as np
import matplotlib.pyplot as plt

# названия файлов
file_names = ["NumPy/signals/signal01.dat", "NumPy/signals/signal02.dat",
              "NumPy/signals/signal03.dat"]

# цикл для трех файлов
for num_of_names in range(len(file_names)):
    f = np.genfromtxt(file_names[num_of_names])
    nf = np.copy(f)
    x = np.linspace(0, f.size, f.size) # ось х
    beg_nf = nf[0:9]
    
    # убираем шумы
    for i in range(1, 9): # фильтрация первых значений
        beg_nf[i] = sum(f[0:i+1])/(i+1)
    
    for i in range(f.size-9): # фильтрация остальных
        nf[9+i] = np.sum(f[i:(10+i)]/10)

    #построение графиков
    fig, axs = plt.subplots(2, figsize = (8,8))
    for a in range(2):
        axs[a].grid()
        if a == 0:
            axs[a].plot(x, f)
            axs[a].set_title("Сырой сигнал " + str(num_of_names+1))
        else:
            axs[a].plot(x, nf)
            axs[a].set_title(f"Сигнал {num_of_names+1} после фильтра ")
    plt.show()