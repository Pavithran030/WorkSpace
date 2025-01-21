import cv2

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Camera', frame)

    # Press 'c' to capture a picture
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Save the frame to a file
        cv2.imwrite('captured_image.jpg', frame)
        print("Picture captured and saved as 'captured_image.jpg'")

    # Press 'q' to quit
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()