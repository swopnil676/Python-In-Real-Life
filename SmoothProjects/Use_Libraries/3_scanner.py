import cv2
from pyzbar.pyzbar import decode
from rich import print

cam = cv2.VideoCapture(0)

while True:

    _, frame = cam.read()

    for qr in decode(frame):

        print(
            f"[bold cyan]QR:[/bold cyan] {qr.data.decode()}"
        )

    cv2.imshow("Scanner", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()