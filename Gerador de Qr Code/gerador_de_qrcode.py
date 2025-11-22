import qrcode

dado = input("Digite o que será transformado em código QR: ")

qr = qrcode.QRCode(
    version=1, 
    box_size=10, 
    border=5 
)

qr.add_data(dado)
qr.make(fit=True)

imagem = qr.make_image(fill_color="black", back_color="white")
imagem.save("Codigo_QR.png")
