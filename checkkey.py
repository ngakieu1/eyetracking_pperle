import cv2

cv2.namedWindow("Test Window", cv2.WINDOW_NORMAL)
print("Press any key (arrow keys, ESC to exit)...")

while True:
    key = cv2.waitKey(0) & 0xFF  # Wait for a key press
    print(f"Key pressed: {key}")

    if key == 27:  # ESC key to exit
        break

cv2.destroyAllWindows()
