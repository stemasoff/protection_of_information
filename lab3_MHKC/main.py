import random

# Пользовательские данные
word = 'Hello, World!'

# Супервозрастающая последовательность
w = (2, 7, 11, 21, 42, 89, 180, 354)

# Число, превосходящее сумму элементов последовательности w
q = sum(w) + random.choice(w)

# Случайное число из интервала [1,q)
r = random.randrange(1, q)

# Открытый ключ
open_key = tuple([(i * r) % q for i in w])

def encoding():
    # Переводим слово в двоичный код
    # Если двоичный код по длине меньше, чем длина ключа, то дописываем 0 перед двоичным словом.
    bit_word = [('0' * (len(open_key) - len(format(ord(i), 'b')))) + format(ord(i), 'b') for i in word]
    print(bit_word)
    # Создание шифра, путем перемножения j-ых элементов i-ого слова и j-ого жлемента ключа
    cipher = list()
    for i in range(len(bit_word)):
        amount = list()
        for j in range(len(open_key)):
            amount.append(int(bit_word[i][j]) * open_key[j])
        cipher.append(sum(amount))
    return cipher

def decoding(cipher):
    # Мультипликативное обратное r по модулю q
    r_inverse = pow(r, q-2, q)

    for element in cipher:
        temp = (element * r_inverse) % q
        
        while temp > min(w):
            temp



print(w)
print(q)
print(r)
print(open_key)
print()
print(encoding())
