import LSB

text = 'Hello, World!1234567891011'
LSB.encoding('Lenna.png', text)
print(LSB.decoding('result.png', len(text)))
