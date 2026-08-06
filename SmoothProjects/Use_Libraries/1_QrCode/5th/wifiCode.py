import qrcode

wifi = "WIFI:S:MyNetwork;T:WPA;P:MyPassword;;"
img = qrcode.make(wifi)
img.save("wifi.png")
print("Scan to connect!")