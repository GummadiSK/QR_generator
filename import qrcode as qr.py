import qrcode as qr
img=qr.make("https://youtu.be/kDzAKXNnAVA?si=ibc6HcYGXfMIJxCt")
img.save("qrcode_youtube.png")

#colour full qrcode
import qrcode as qr
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr.add_add("https://youtu.be/kDzAKXNnAVA?si=ibc6HcYGXfMIJxCt")
img=qr.make_image(fill_color="red",back_color="blue")
img.save("qrcode_youtube.png")