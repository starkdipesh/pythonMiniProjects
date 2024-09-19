import qrcode
import qrcode.constants

# youtube link

youtubeLink="https://youtu.be/KmqKHRkLECU?si=kAGYEln0aCVgVgS9"

# Geneerate qr code 
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(youtubeLink)
qr.make(fit=True)

# create image from qrcode 
img=qr.make_image(fill='black',back_color='white')

# save qr code image
img.save("hetpatel.png")