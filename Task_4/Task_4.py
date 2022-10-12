# Задача 4: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах. 

s = input("Введите текст для сжатия: ")

def compres(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]: # Если индекс текста больше чем 1
            count += 1 # то счетчик количества элементов увеличивается.Например WW ТО 2W
        else:
            res += str(count) + txt[i] # Иначе пишем что элемент 1
            count = 1 # Например 1M
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res += str(count) + txt[-1]
    return res

def decompres(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha(): # Если в индекс записана буква 
            number += txt[i] # то заносим ее в строку
        else:
            res += txt[i] * int(number) # иначе цифру умножаем на букву
            number = '' # Например 3R = 3 * R = RRR
    return res

print(f"Сжатый текст: {compres(s)}")
print(f"Дешифрованный текст: {decompres(compres(s))}")