
import cv2
import os

# ==========================================
# APF3 - DETECTOR DE LAPTOP
# Ingeniería Civil - Visión Computacional
# ==========================================

# Conexión con DroidCam
cap = cv2.VideoCapture(
    "http://10.80.162.232:4747/video"
)

# Cargar el modelo Haar Cascade de laptop
ruta_modelo = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "classifier",
    "cascade.xml"
)

LaptopClassif = cv2.CascadeClassifier(ruta_modelo)

# Verificar el modelo
if LaptopClassif.empty():
    print("Error: No se pudo cargar el modelo de laptop")
    cap.release()
    exit()

if not cap.isOpened():
    print("Error: No se pudo conectar con DroidCam")
    exit()

print("Detector de laptop iniciado correctamente")
print("Presiona ESC para finalizar")

while True:

    ret, frame = cap.read()

    if not ret:
        print("No se recibió imagen de DroidCam")
        break

    # Convertir a escala de grises
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Reducir ruido
    gray = cv2.equalizeHist(gray)

    # Detección de laptops
    laptops = LaptopClassif.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=12,
        minSize=(70, 70),
        maxSize=(500, 500)
    )

    for (x, y, w, h) in laptops:

        # Rectángulo alrededor del objeto
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Etiqueta
        cv2.putText(
            frame,
            "LAPTOP",
            (x, max(y - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

    cv2.imshow(
        "APF3 - Detector de Laptop",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
