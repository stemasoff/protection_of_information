# Пре-альфа версия, сделано наспех, чисто чтобы работало...
import random
# Пользовательские данные
word = 'Hello World!'
# Супервозрастающая последовательность
w = (2, 7, 11, 21, 42, 89, 180, 390)

# Простое число, превосходящее сумму элементов последовательности w
q = 881

# Случайное число из интервала [1,q)
r = random.randrange(1, q)

# Открытый ключ
open_key = tuple([(i * r) % q for i in w])
print(open_key)

def encoding(word, open_key):
    # Переводим слово в двоичный код
    # Если двоичный код по длине меньше, чем длина ключа, то дописываем 0 перед двоичным словом.
    bit_word = [('0' * (len(open_key) - len(format(ord(i), 'b')))) + format(ord(i), 'b') for i in word]

    # Создание шифра, путем перемножения j-ых элементов i-ого слова и j-ого жлемента ключа
    cipher = list()
    for i in range(len(bit_word)):
        amount = list()
        for j in range(len(open_key)):
            amount.append(int(bit_word[i][j]) * open_key[j])
        cipher.append(sum(amount))
    return cipher

def decoding(cipher, w, r, q):
    # Мультипликативное обратное r по модулю q
    r_inverse = pow(r, q-2, q)
    decoded_dig = list()
    decoded_text = str()

    for i in range(len(cipher)):
        temp = (cipher[i] * r_inverse) % q
        temp_w = list(w)

        decoded_dig.append('0' * len(w))

        # Раскладываем временную переменную по делителям
        while temp >= min(w):
            temp_w.append(temp)
            temp_w.sort()

            if temp_w.count(temp) > 1:
                decoded_dig[i] = decoded_dig[i][:temp_w.index(temp)] + '1' + decoded_dig[i][temp_w.index(temp)+1:]
                temp = temp - temp_w[temp_w.index(temp)]
            else:
                decoded_dig[i] = decoded_dig[i][:temp_w.index(temp)-1] + '1' + decoded_dig[i][temp_w.index(temp):]
                temp = temp - temp_w[temp_w.index(temp) - 1]
        decoded_text = decoded_text + chr(int(decoded_dig[i],2))


    return decoded_text

print('Исходный текст:', word)
print('Ваш ключ:\nR:',r ,'\nw:', w, '\nq:', q)

cipher = encoding(word, open_key)
decoded_text = decoding(cipher, w, r, q)

print('Зашифрованный текст:', cipher)
print('Расшифрованный текст:', decoded_text)
