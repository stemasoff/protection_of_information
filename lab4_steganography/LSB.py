# Не готово, в планах еще подключить ГСПЧ для стегоконтейнера
from PIL import Image, ImageDraw


def encoding(picture, text):
    '''
    Функция шифрования текста в картинке.
    :param picture: картинка, в которую будет помещен стего
    :param text: текст, который необходимо зашифровать
    :return:
    '''
    img = Image.open(picture)
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    exitFlag = False
    temp_cipher = ''

    for i in text:
        # Цикл для перевода букв из текста в двоичный код.
        temp_cipher = temp_cipher + '0' * (8 - len(format(ord(i), 'b'))) + format(ord(i), 'b')
    cipher = [temp_cipher[i:i + 2] for i in range(0, len(temp_cipher), 2)]
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
    print('Длина зашифрованного сообщения: {}'.format(len(text)))


def decoding(picture, lendth):
    '''
    Функция раскодирования.
    :param picture: Картинка с зашифрованными данными
    :param lendth: Длина зашифрованного сообщения
    :return:
    '''
    img = Image.open(picture)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    cipher = ''
    decoded_text = ''

    try:
        for i in range(height):
            for j in range(width):
                # Считываем последние два бита в каождом из каналов
                for color in range(3):
                    cipher = cipher + format(pix[i, j][color], 'b')[-2:]
                    if len(cipher) == lendth * 8:
                        raise Exception
    except Exception:
        # Переводим двоичный код в текст
        text_cipher = [cipher[i:i + 8] for i in range(0, len(cipher), 8)]
        for i in text_cipher:
            decoded_text = decoded_text + chr(int(i, 2))
        return decoded_text