import qrcode

data = 'Python Project QRcode reader mark2'
qr = qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'Aqua', back_color = 'black')
img.save('C:/Users/kb290/Desktop/qr code/myqrcode(colored).png')