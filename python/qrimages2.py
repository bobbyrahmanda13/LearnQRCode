import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer 
from qrcode.image.styles.colormasks import SolidFillColorMask
# from qrcode.image.styles.colormasks import RadialGradiantColorMask
# from PIL import Image

# Fungsi untuk menambahkan gambar ditengah QR Code
# def addLogo(qr_code, gambar):
#     qr_code = qr_code.convert("RGBA")
#     gambar = gambar.resize((50, 50))  # Ubah ukuran gambar sesuai kebutuhan
#     posisi = ((qr_code.size[0] - gambar.size[0]) // 2, (qr_code.size[1] - gambar.size[1]) // 2)
#     qr_code.paste(gambar, posisi, gambar)
#     return qr_code


# # Tautan WhatsApp
# whatsapp_link = "085274620281"
# # Tautan YouTube
# github_link = "github.com/bobbyrahmanda13"
# # Tautan Instagram
# instagram_link = "instagram.com/0.0_rahman_0.0/"
# # Tautan Telegram
# telegram_link = "t.me/Rahman_0000"
# # Tautan Website
# web_link = "bobbyrahmanda13.netlify.app"
# # Tautan Twitter
# twitter_link = "twitter.com/r4hm4n1309"


# Menggabungkan tautan menjadi satu teks
combined_text = f"https://rismaexpress.github.io/rismaexpress/"

# Membuat QR code
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,)
qr.add_data(combined_text)
qr.make(fit=True)

# Menyimpan QR code sebagai gambar PNG
qr_image = qr.make_image(
    image_factory=StyledPilImage, 
    module_drawer=RoundedModuleDrawer(), eye_drawer=RoundedModuleDrawer(), 
    color_mask=SolidFillColorMask(back_color=(255,255,255), front_color=(0,0,0))
    # color_mask=RadialGradiantColorMask(back_color=(255,255,255), edge_color=(0,0,0), center_color=(100,100,100))
)

# logo = Image.open("image/g.png")
# qrCodeWithImage = addLogo(qr_image, logo)
qr_image.save("lala.png")
