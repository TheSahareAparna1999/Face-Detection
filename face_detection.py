# OpenCV program to detect faces in real time

# import cv2
import cv2

# load the pre-trained haarcascade_frontalface_default XML classifier
detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# capture frame from a webcam
Cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

    # read frame from a webcam
    ret, image = Cap.read()

    # convert color image to gray scale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces of different sizes from the frame
    face = detect.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle around the faces
    for (x, y, w, h) in face:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 3)

    # Display an image in a window
    cv2.imshow('Camera', gray)

    # press 'ESC' to quit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release captured images
Cap.release()

# Destroy all windows
cv2.destroyAllWindows()
