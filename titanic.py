import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_parquet('titanic.parquet') # чтение файла
df.to_csv('titanic.parquet', index=False) # сохранение в csv
df_csv = pd.read_csv('titanic.parquet') # чтение файла
quantity_passengers = df_csv.groupby('Pclass').size() # количество элементов в каждой группе
survived = df_csv[df_csv['Survived'] == 1].groupby('Pclass').size() / quantity_passengers * 100 # процент выживших
not_survived = df_csv[df_csv['Survived'] == 0].groupby('Pclass').size() / quantity_passengers * 100 # процент умерших
survival_data = pd.DataFrame({
    'Выжившие': survived,
    'Не выжившие': not_survived
})
# ✨график✨
ax = survival_data.plot(kind='bar', stacked=True, color=['green', 'red']) # столбчатая диаграмма, столбцы будут накладываться друг на друга
ax.set_xlabel('Класс билета') # название оси X
ax.set_ylabel('Доля пассажиров (%)') # название оси Y
ax.set_title('Выживаемость пассажиров в зависимости от класса билета') # заголовок для графика
ax.legend(title='Статус')
plt.show()