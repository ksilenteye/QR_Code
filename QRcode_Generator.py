import qrcode

data = 'Python Project QRcode reader'

img = qrcode.make(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'blue', back_color = 'black')

img.save('C:/Users/kb290/Desktop/qr code/myqrcode.png')