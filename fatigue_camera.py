import cv2

def detect_fatigue():

    face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    cam = cv2.VideoCapture(0)

    fatigue = False

    while True:
        ret, frame = cam.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            roi_gray = gray[y:y+h, x:x+w]

            eyes = eye.detectMultiScale(roi_gray)

            if len(eyes) == 0:
                fatigue = True

        cv2.imshow("Face Scan", frame)

        if cv2.waitKey(1) == 27 or fatigue:
            break

    cam.release()
    cv2.destroyAllWindows()

    return fatigue
