import qrcode as qr
img = qr.make("https://www.youtube.com/@wscubetech")
img.save("WsCube_Tech.png")