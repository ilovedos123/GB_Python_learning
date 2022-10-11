# 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'Как хорошо, что существуют автобусы! Можно проводить калибровку семян иным способом. Для чего их пропускают через калибровочное сито с ячейками нужного размера.'
word_list = list(text.split())
for i in word_list:
    if 'а' in i and 'б' in i and 'в' in i:
        word_list.remove(i)
result_text = " ".join(map(str, word_list))
print(result_text)
