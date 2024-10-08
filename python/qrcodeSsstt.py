import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
# qr.add_data('26-Mar-2016 | ALT/PDG/188 | KURSI DIV. RETUR | H.PEROLEHAN RP 315000')
qr.add_data('26-Mar-2016 | ALT/PDG/186 | KURSI DIV. RETUR | H.PEROLEHAN RP 315000')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('Sssssttt1.png')
