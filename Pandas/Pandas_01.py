import pandas as pd
import numpy as np

# считываем файл
df = pd.read_csv('Pandas/transactions.csv', delimiter=',')

# Максимальные платежи "Ok"
print(df.sort_values(by = 'SUM', ascending = False).loc[df["STATUS"] == "OK"][0:3])

print("\n", "=" * 20, "\n")

# Только Umbrella
Um = df[df["CONTRACTOR"] == "Umbrella, Inc"]

# Платежи в Umbrella
Um_OK = Um[Um["STATUS"] == "OK"] # Платежи Umbrella только "Ok"
print("Сумма Umbrella: ", Um_OK[Um_OK["STATUS"] == "OK"].loc[:, "SUM"].sum())