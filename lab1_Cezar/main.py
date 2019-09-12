# Объявление русского алфавита в нижнем и верхнем регистре
alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
capital_alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# Функция для кодирования сообщения кодом Цезаря
def code(ofset, text):
    """
    :param ofset: Смещение
    :param text:  Текст для кодирования(string)
    :return:  Закодированный текст(string)
    """
    encoded_text = str()
    for i in text:
        if i in alph:
            # Замена букв нижнего регистра
            encoded_text = encoded_text + alph[(alph.index(i) + ofset) % len(alph)]
        elif i in capital_alph:
            # Замена букв верхнего регистра
            encoded_text = encoded_text + capital_alph[(capital_alph.index(i) + ofset) % len(capital_alph)]
        else:
            # Если символа нет в алфавите, его оставляет нетронутым
            encoded_text = encoded_text + i
    return encoded_text
# Реализация работы с пользователем
action = int(input('Выберите действие. Зашифровать - 1, Расшифровать - 2: '))
# Шифрование
if action == 1:
    # Открываем файл, который нужно зашифровать
    with open('text.txt', 'r', encoding='utf-8') as inpt:
        text = inpt.read()
    shift = int(input('Введите смещение: '))        # Инициализация смещения
    crypt = code(shift, text)       # Вызов функции с пользовательскими данными
    with open('encoded.txt', 'w', encoding='utf-8') as out:
        out.write(crypt)
# Взлом шифра
elif action == 2:
    with open('encoded.txt', 'r', encoding='utf-8') as inpt:
        crypt = inpt.read()
    # Сбор статистики в список
    stat = [int(crypt.lower().count(i)) for i in alph]
    '''
    Вычисляем смещение для расшифровки закодированного текста
    15 - константа, соответвующая индексу буквы "о", самой частотной букве
    в русском языке.
    '''
    decode = 15 - stat.index(max(stat))
    decode_text = code(decode, crypt)
    with open('decoded.txt', 'w', encoding='utf-8') as out:
        out.write(decode_text)
else:
    print('Неверный ввод!')
