import pandas as pd
import matplotlib.pyplot as plt

# считываем файл в df
df = pd.read_csv('Pandas/flights.csv', delimiter=',')

df.sort_values(by = "CARGO", ascending = False)

# Number of flights
# df_01 = df.loc[:"CARGO"]
# df_01 = df_01.groupby(["CARGO"]).count()

df_01 = df.groupby("CARGO")["CARGO"].count()

# Total weight
df_02 = df.loc[:, ["CARGO","PRICE"]]
df_02 = df_02.groupby(["CARGO"]).sum()

# Total price
df_03 = df.loc[:, ["CARGO","WEIGHT"]]
df_03 = df_03.groupby(["CARGO"]).sum()


#строим графики
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
df_01.plot(ax=axs[0], title="Number of flights", kind='bar', legend = False)
df_02.plot(ax=axs[1], title="Total weight", kind='bar', legend = False)
df_03.plot(ax=axs[2], title="Total price", kind='bar', legend = False)

plt.show()



