import matplotlib.pyplot as plt
f1 = open("MatPlotLib/tests/DAT1.dat", 'r')
f2 = open("MatPlotLib/tests/DAT2.dat", 'r')
f3 = open("MatPlotLib/tests/DAT3.dat", 'r')
f4 = open("MatPlotLib/tests/DAT4.dat", 'r')
f5 = open("MatPlotLib/tests/DAT5.dat", 'r')

a1, a2, a3, a4, a5 = [], [], [], [], []

# записываем данные из файлов
for line in f1:
    a1.append(line)
for line in f2:
    a2.append(line)
for line in f3:
    a3.append(line)
for line in f4:
    a4.append(line)
for line in f5:
    a5.append(line)
# количество данных в каждом файле
n1,n2,n3,n4,n5 = int(a1[0]), int(a2[0]), int(a3[0]), int(a4[0]), int(a5[0])

x1, x2, x3, x4, x5, y1, y2, y3, y4, y5 = [], [], [], [], [], [], [], [], [], []
# записываем значения для x и y
for i in range(1,n1+1):
    b = a1[i].split(" ")
    x1.append(float(b[0]))
    y1.append(float(b[1]))
for i in range(1,n2+1):
    b = a2[i].split(" ")
    x2.append(float(b[0]))
    y2.append(float(b[1]))
for i in range(1,n3+1):
    b = a3[i].split(" ")
    x3.append(float(b[0]))
    y3.append(float(b[1]))
for i in range(1,n4+1):
    b = a4[i].split(" ")
    x4.append(float(b[0]))
    y4.append(float(b[1]))
for i in range(1,n5+1):
    b = a5[i].split(" ")
    x5.append(float(b[0]))
    y5.append(float(b[1]))

# построение графиков (шестой график пустой)
fig, axs = plt.subplots(3, 2)
axs[0][0].scatter(x1, y1, color = 'r', s = 10)
axs[0][0].set_aspect(aspect = "auto")
axs[0][1].scatter(x2, y2, color = 'g', s = 10)
axs[0][1].set_aspect(aspect = "auto")
axs[1][0].scatter(x3, y3, color = 'b', s = 10)
axs[1][0].set_aspect(aspect = "auto")
axs[1][1].scatter(x4, y4, color = 'y', s = 4)
axs[1][1].set_aspect(aspect = "auto")
axs[2][0].scatter(x5, y5, color = 'deeppink', s = 1)
axs[2][0].set_aspect(aspect = "auto")
plt.show()