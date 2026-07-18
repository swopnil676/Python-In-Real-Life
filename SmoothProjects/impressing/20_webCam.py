import cv2
import screen_brightness_control as sbc

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate average brightness (0-255)
    brightness = gray.mean()

    # Convert brightness to screen brightness (20-100)
    screen_level = int((brightness / 255) * 100)
    screen_level = max(20, min(screen_level, 100))

    # Set monitor brightness
    sbc.set_brightness(screen_level)

    # Show webcam feed
    cv2.imshow("Auto Brightness", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()