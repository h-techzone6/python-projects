import qrcode as qr
img = qr.make("https://www.python.org/")
img.save("myqr.png")