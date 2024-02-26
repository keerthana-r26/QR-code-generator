import qrcode
qr = qrcode.QRCode(
    version=12,
    box_size=10,
    border=2
)
data = "https://pacewisdom.com/"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("advanced.png")
