import cv2

# Load Haar Cascade model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load Image
image = cv2.imread("images/sample1.jpg")  # Make sure this file exists
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display output
cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

