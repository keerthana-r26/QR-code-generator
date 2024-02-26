import qrcode

myqr = qrcode.make("https://swapnodaya.com/")
myqr.save("myqr.png")
