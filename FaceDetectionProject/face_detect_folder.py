import cv2
import os

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Folder with images
folder_path = "images/"

# Loop through files
for file in os.listdir(folder_path):
    if file.endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(folder_path, file)
        image = cv2.imread(img_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow(f"Faces in {file}", image)
        cv2.waitKey(5000)  

cv2.destroyAllWindows()

