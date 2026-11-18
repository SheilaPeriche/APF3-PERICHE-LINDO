
import cv2

ruta = "classifier/cascade.xml"

detector = cv2.CascadeClassifier(ruta)

cap = cv2.VideoCapture("http://10.80.162.232:4747/video")

if not cap.isOpened():
    print("Error al conectar con DroidCam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    laptops = detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=8,
        minSize=(40, 40)
    )

    for (x, y, w, h) in laptops:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(
            frame,
            "LAPTOP",
            (x, max(y-10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Prueba del detector de laptop", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
