import matplotlib.pyplot as plt

data = []
with open("MatPlotLib/tests/LABA_2.dat", 'r') as f:
    for line in f:
        data.append([float(x) for x in line.split()])

data_count = 0
frames_count = 0

# построение графиков
fig, axs = plt.subplots(3,2,figsize=(12, 12))
# берем соответствующие графику значения из data
for i in range(3):
    for j in range(2):
        axs[i][j].plot(data[data_count], data[data_count+1])
        axs[i][j].set(xlim = (0,max(data[0])), ylim = (-9,12))
        axs[i][j].set_title(f"Frame {frames_count}")
        axs[i][j].grid()
        frames_count +=1
        data_count += 2 # т.к одной frames_count соответствует два data_count

plt.show()