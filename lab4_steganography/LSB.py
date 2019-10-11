from PIL import Image, ImageDraw


def encoding(text):
    '''
    Функция шифрования текста в картинке.
    :param text: текст, который необходимо зашифровать
    :return: создает картинку с зашифрованным текстом
    '''
    img = Image.open('Lenna.png')
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    exitFlag = False
    text_cipher = ''

    for i in text:
        # Цикл для перевода букв из текста в двоичный код.
        text_cipher = text_cipher + '0' * (8 - len(format(ord(i), 'b'))) + format(ord(i), 'b')
    cipher = [text_cipher[i:i + 2] for i in range(0, len(text_cipher), 2)]

    for i in range(height):
        for j in range(width):
            # Считываем RGB пиксели в двоичном виде
            r = format(pix[i, j][0], 'b')
            g = format(pix[i, j][1], 'b')
            b = format(pix[i, j][2], 'b')
            try:
                # Меняем последние два пикселя в каждом из каналов на наши данные
                r = r[:6] + cipher.pop(0)
                g = g[:6] + cipher.pop(0)
                b = b[:6] + cipher.pop(0)
                draw.point((i, j), (int(r, 2), int(g, 2), int(b, 2)))
            except IndexError:
                draw.point((i, j), (int(r, 2), int(g, 2), int(b, 2)))
                exitFlag = True
                break
        if exitFlag is True:
            break

    img.save('result.png', 'png')


def decoding(image, lendth):
    '''
    Функция раскодирования.
    :param image: Картинка с зашифрованными данными
    :param lendth: Длина зашифрованного сообщения
    :return:
    '''
    img = Image.open(image)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    cipher = ''
    exitFlag = False
    decoded_text = ''

    for i in range(height):
        for j in range(width):
            # Считываем последние два
            cipher = cipher + format(pix[i, j][0], 'b')[-2:]
            cipher = cipher + format(pix[i, j][1], 'b')[-2:]
            cipher = cipher + format(pix[i, j][2], 'b')[-2:]
            if (i + 1) * (j + 1) >= int(lendth * (4 / 3)):
                exitFlag = True
                break
        if exitFlag == True:
            break
    # Переводим двоичный код в текст
    text_cipher = [cipher[i:i + 8] for i in range(0, len(cipher), 8)]
    for i in text_cipher:
        decoded_text = decoded_text + chr(int(i, 2))

    return decoded_text




'''
Мои попытки сделать статистический анализ пикселей и взломать шифр
def decoding(image):
    img = Image.open(image)
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    red_array = list()

    for i in range(height):
        for j in range(width):
            red_array.append(pix[i, j][0])

    histogram = list()
    expected = list()
    observed = list()

    for i in range(0, 256):
        histogram.append(red_array.count(i))

    for k in range(0, len(histogram) // 2):
        expected.append(((histogram[2 * k] + histogram[2 * k + 1]) / 2))
        observed.append(histogram[2 * k])
        x = (observed[k] - expected[k]) ** 2 / expected[k]
    print(expected)
    print(observed)
'''
