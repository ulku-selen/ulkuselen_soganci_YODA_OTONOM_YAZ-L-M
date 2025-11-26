import cv2
from collections import deque
import time

# Haar cascade yükleme
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Kamera ac
cap = cv2.VideoCapture(0)

# Son 60 koordinat 
points = deque(maxlen=60)

face_detected = False
start_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) > 0:
        # Yüz tespit edildi
        if not face_detected:
            face_detected = True
            start_time = time.time()

        (x, y, w, h) = faces[0]
        cx = x + w//2
        cy = y + h//2

        # Bounding box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        # Merkez koordinatlarını yaz
        cv2.putText(frame, f"Center: ({cx}, {cy})", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        # Kuyruğa ekle
        points.append((cx, cy))

        # Süre hesapla
        elapsed = int(time.time() - start_time)
        cv2.putText(frame, f"{elapsed} s", (frame.shape[1]-100, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    else:
        # Yüz kaybolduysa
        face_detected = False
        points.clear()

    # Son 60 noktanın çizilmesi
    for i in range(1, len(points)):
        cv2.line(frame, points[i-1], points[i], (0, 0, 255), 2)

    cv2.imshow("Face Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
