import pandas as pd
import matplotlib.pyplot as plt






#создание таблицы данных
url = 'https://ru.wikipedia.org/wiki/%D0%90%D1%82%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F_%D1%8D%D0%BD%D0%B5%D1%80%D0%B3%D0%B5%D1%82%D0%B8%D0%BA%D0%B0_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'
tabel = pd.read_html(url, decimal=',', thousands="'")[1]
row = tabel.columns
data = tabel.to_numpy()
rows = []
for i in row:
    rows.append(i)
sl = {}
for i in rows:
    sl[i] = []
k = 0
for i in rows:
    for j in range(len(data)):
        if k == 0:
            sl[i].append(data[j][k][0:4])
        elif '\xa0' in str(data[j][k]):
            sl[i].append(data[j][k].replace('\xa0', ''))
        elif pd.isna(data[j][k]):
            sl[i].append(0)
        else:
            sl[i].append(data[j][k])
    k += 1
tabel = pd.DataFrame(sl, index=sl['Год'])

#сортировка
tabel = tabel.sort_values(['Выработка млрд кВт•ч'])
#Добавление столбца
tabel['Разница между выробаткой и реализацией'] = tabel['Выработка млрд кВт•ч'] - tabel['Реализация млрд кВт•ч']
#Выборка данных по условию
print(tabel[tabel['Реализация млрд кВт•ч'] > 0])
#Выборка данных по индексам
print(tabel.iloc[2:4, 0:3])
#Рассчет данных по сортированым значениям
tabel2 = tabel[tabel['Реализация млрд кВт•ч'] > 0]
print('Среднее значение не нулевых реализованных мощностей', tabel['Реализация млрд кВт•ч'].sum()/ len(tabel['Реализация млрд кВт•ч']), 'млрд кВт•ч')
#визуализация
tabel = tabel.sort_values(['Год'])
tabel.plot(x = 'Год', y = 'Выработка млрд кВт•ч', kind='bar',)
tabel.plot(x = 'Год', y = 'Выработка млрд кВт•ч', kind='pie', subplots=True, legend=False)
tabel.plot(x = 'Год', y = 'Выработка млрд кВт•ч', subplots=True)
plt.show()
tabel.to_excel('Атомная энергетика.xlsx', index = False)
