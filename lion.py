import docx #библиотека для работы с вордовскими доками
from collections import Counter # всем было лень считать через цикл, так что и мне тоже (не осуждайте, пожалуйста)
import re # для работы с текстом 
import pandas as pd 
import matplotlib.pyplot as plt # для графика
doc = docx.Document('lion.docx') # открытие дока
num_par = len(doc.paragraphs) # количество абзацев
word_list = [] # список слов без повторений 
a = [] 
rus_let = re.compile(r'[а-яё]', re.IGNORECASE) # регулярное выражение или типа того, игнорирующее заглавные буквы
rus_text = [] # список для всего текста
rus_word = re.compile(r'\b[а-яё]+\b',re.IGNORECASE) # регулярное выражение или типа того 
for paragraph in doc.paragraphs: # для каждого абзаца из абзацев...
    text = paragraph.text.lower() # весь текст в нижний регистр
    words = rus_word.findall(text) # находим русские слова и добавляем в список
    letters = rus_let.findall(text) # тоже самое, но с буквами
    a.extend(letters) # добавляем буквы в общий список
    for word in words: #ммм цикл
        rus_text.append(word)
        if word not in word_list: # проверка на наличие слов в списке 
            word_list.append(word) # добавления слова, если его нет в списке 
rus_text_len = len(rus_text) # количество слов в списке
word_counts = Counter(rus_text) # частота встречаемости слов (на ленивом)
#очень красивый словарик
dict_word = {
    'Слово': list(word_counts.keys()),
    'Частота встречи,раз': list(word_counts.values()),
    'Частота встречи в %': [round((count / rus_text_len) * 100, 2) for count in word_counts.values()]
}
df_word = pd.DataFrame(dict_word)
doc_word = docx.Document() # новый док
doc_word.add_heading('Встречаемость слов в тексте', 0) # заголовок для приличия
table = doc_word.add_table(rows=1, cols=3) # таблица с одной строкой и тремя колонками 
hdr_cells = table.rows[0].cells # cells - используем для доступа к конкретным ячейкам строки, чтобы заполнить их содержимым
hdr_cells[0].text = 'Слово' 
hdr_cells[1].text = 'Частота встречи,раз'
hdr_cells[2].text = 'Частота встречи в %'
for i in range(len(df_word)):
    row_cells = table.add_row().cells # новые строки в таблицу                                        
    row_cells[0].text = df_word.loc[i, 'Слово'] # loc - выбор строки с индексом [i]
    row_cells[1].text = str(df_word.loc[i, 'Частота встречи,раз'])
    row_cells[2].text = str(df_word.loc[i, 'Частота встречи в %'])
doc_word.save('Встречаемость_слов.docx') # сохранение дока
letters_counts = Counter(a) #частота встречаемости букв (тоже на ленивом)
df_letter = pd.DataFrame(letters_counts.items(),columns=['Буквы','Количество'])
df_letter['Количество'] = pd.to_numeric(df_letter['Количество']) # преобразования значений в столбцах в числовой тип данных
plt.figure(figsize=(10, 6))# ширина - 10 дюймов, высота — 6
plt.bar(df_letter['Буквы'], df_letter['Количество'], color='skyblue') # столбчатая диаграмма
plt.xlabel('Буквы') # ось X - буквы
plt.ylabel('Количество') # ось Y - количество
plt.title('Встречаемость букв в тексте') # заголовок для приличия
plt.grid(True) # отображение сетки на графике
plt.show() # вывод графика
