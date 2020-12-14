import pandas as pd
import matplotlib.pyplot as plt

# названия файлов для считывания
names = ["Pandas/students_info.xlsx", "Pandas/results_ejudge.html"]

# считываем файлы
df1 = pd.read_excel(names[0], sheet_name="logins")
df2 = pd.read_html(names[1])

# объединяем df1 и df2
df3 = pd.merge(df1, df2[0], left_on="login", right_on="User")

# среднее кол-во задач
faculty = df3.groupby("group_faculty").mean()
group = df3.groupby("group_out").mean()

# строим графики
fig, axs = plt.subplots(1, 2, figsize = (10,6))
# по факультетам
faculty["Solved"].plot(ax=axs[0], kind='bar', ylim = (0,8))
# по группам
group["Solved"].plot(ax=axs[1], kind='bar', ylim = (0,8))

plt.show()

# ответы на вопросы лабы
print("Из каких групп: ",
      *pd.unique((df3[(df3["H"] > 10) | (df3["G"] > 10)])["group_faculty"]))
print("В какие IT группы:",
      *pd.unique((df3[(df3["H"] > 10) | (df3["G"] > 10)])["group_out"]))