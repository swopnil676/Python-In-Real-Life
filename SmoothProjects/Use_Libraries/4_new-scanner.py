import qrcode
from PIL import Image

# Create QR Code
qr = qrcode.make(
    "https://leetcode.com/.com").convert("RGB")

# Open logo image
logo = Image.open(r"A:\CODING\ADVANCED PYTHON\SmoothProjects\SimpleTypes\logo.png")

# Resize logo
logo = logo.resize((80, 80))

# Position logo at center
pos = (
    (qr.size[0] - 80) // 2,
    (qr.size[1] - 80) // 2
)

# Paste logo into QR
qr.paste(logo, pos)

# Show QR code
qr.show()

# Save QR code
qr.save("qr_with_logo.png")