# пандас, чтобы работать с табличками
import pandas as pd
# матплотлиб для графика
import matplotlib.pyplot as plt
# читаем исходный файл в формате parquet
df = pd.read_parquet('titanic.parquet')
# сохраняем его уже в обычный csv (чтобы потом было проще)
df.to_csv('titanic.csv', index=False)
# читаем только что сохранённый csv
df_csv = pd.read_csv('titanic.csv')
# считаем, сколько пассажиров было в каждом классе
quantity_passengers = df_csv.groupby('Pclass').size()
# процент выживших по классам
survived = df_csv[df_csv['Survived'] == 1].groupby('Pclass').size() / quantity_passengers * 100
# процент тех, кто не выжил
not_survived = df_csv[df_csv['Survived'] == 0].groupby('Pclass').size() / quantity_passengers * 100
# собираем всё в одну табличку для графика
survival_data = pd.DataFrame({
    'Выжившие': survived,
    'Не выжившие': not_survived
})
# делаем столбчатую диаграмму, где столбцы накладываются друг на друга
ax = survival_data.plot(kind='bar', stacked=True, color=['green', 'red'])
# подписываем ось X
ax.set_xlabel('Класс билета')
# подписываем ось Y
ax.set_ylabel('Доля пассажиров (%)')
# пишем заголовок
ax.set_title('Выживаемость пассажиров в зависимости от класса билета')
# добавляем легенду
ax.legend(title='Статус')

plt.show()
