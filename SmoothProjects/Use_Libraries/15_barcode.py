from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image, ImageEnhance

code = EAN13(
    "123456789102",
    writer=ImageWriter()
)

filename = code.save("ean13_barcode")

img = Image.open(filename)

img = ImageEnhance.Color(img).enhance(4)

img.show()