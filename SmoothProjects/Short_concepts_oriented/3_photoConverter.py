import cv2

# noob version
# img = cv2.imread("Screenshot 2026-06-13 203908.png")
# sharp = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
# cv2.imwrite("hd_photo.jpg", sharp)
# print("Photo enhanced! 📸")

# Better Version
img = cv2.imread(r"A:\CODING\ADVANCED PYTHON\SmoothProjects\Short_concepts_oriented\Screenshot 2026-06-13 203908.png")

if img is None:
    print("Image not found!")
else:
    sharp = cv2.detailEnhance(
        img,
        sigma_s=10,
        sigma_r=0.15
    )

    cv2.imwrite("hd_photo.jpg", sharp)
    print("Photo enhanced successfully! 📸")