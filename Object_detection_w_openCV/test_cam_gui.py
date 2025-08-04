import cv2

cap = cv2.VideoCapture(0)  # change to 1 or 2 if needed

if not cap.isOpened():
    print("❌ Camera not detected.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    cv2.imshow("Camera Test", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("✅ Exiting...")
        break

cap.release()
cv2.destroyAllWindows()

