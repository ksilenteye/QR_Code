from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/kb290/Desktop/qr code/Expriment.jpg')

result = decode(img)

print(result)