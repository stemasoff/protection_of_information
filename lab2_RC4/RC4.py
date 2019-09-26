# coding=utf-8
from operator import xor

def s_block_generate(text_or_cipher, key, n):
    '''
    :param text_or_cipher: Текст или шифр, на основе которого нужно сгенерировать s_block
    :param key: Пользовательский ключ
    :param n: Количество бит
    :return: Ключевлой поток s_block(list int)
    '''

    #   Инициализация KSA(key-scheduling algorithm)
    #   s - последовательность битов
    #   temp_key - переменная, длинной в s, которая состоит из ключа key
    s = [i for i in range(2**n)]
    temp_key = [key[i % len(key)] for i in s]

    #   Перемешиваем массив, путем перестановок, определяемых ASCII-кодом ключа
    j = 0
    for i in range(2**n):
        j = (j + s[i] + ord(temp_key[i])) % 2**n
        s[i], s[j] = s[j], s[i]

    #   Генерация псевдослучайного кода PRGA(pseudo-random generation algorithm)
    #   s_block - переменная, которая будет содержать перестановку 2^n возможных значений слова
    s_block = list()
    i, j = 0, 0
    length_text = len(text_or_cipher)
    '''
    Генератор ключевого потока RC4 переставляет значения, хранящиеся в s,
    и каждый раз выбирает различное значение из s в качестве результата. В одном цикле определяется
    одно n-битное слово из ключевого потока.
    '''
    while length_text > 0:
        i = (i + 1) % 2**n
        j = (j + s[i]) % 2**n
        s[i], s[j] = s[j], s[i]
        s_block.append(s[(s[i] + s[j]) % 2**n])
        length_text -= 1
    return s_block

def encode(text, s_block):
    '''
    Шифрование
    :param Text: Текст, который нужно зашифровать
    :param s_block: Ключевой поток
    :return: Шифр(list int)
    '''

    # Сложение по модулю 2 i-го элемента ключевого потока и ascii-кода символа в тексте.
    cipher = [xor(ord(text[i]), s_block[i]) for i in range(len(text))]
    return cipher


def decode(cipher, s_block):
    '''
    Расшифровка
    :param cipher: Шифр
    :param s_block: Ключевой поток
    :return: Расшифрованный текст(str)
    '''
    decoded_text = str()

    abc = [xor(int(cipher[i]), int(s_block[i])) for i in range(len(cipher))]
    for i in abc:
        decoded_text = decoded_text + chr(i)
    return decoded_text