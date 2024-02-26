import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


myqr = qrcode.make("https://swapnodaya.com/")
myqr.save("myqr2.png")

b = decode(Image.open('myqr2.png'))
print(b[0].data.decode("ascii"))
