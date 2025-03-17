import cv2

cap = cv2.VideoCapture(0)  # Try with 1 if 0 doesn’t work
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Test Frame", frame)
        cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()