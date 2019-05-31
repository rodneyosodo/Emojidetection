import cv2
import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
face_cascade = cv2.CascadeClassifier("Models/haarcascade_frontalface_alt2.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Models/trainer.yml")

labels = {}
with open("Models/labels.pkl", "rb") as f:
	og_labels = pickle.load(f)
	labels = {v:k for k, v in og_labels.items()}

class VideoStream():
    def __init__(self):
        #Constructor that returns a video camera input.
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        #Class destructor.
        self.video.release()

    def get_frame_grs(self):
        #Camera input for processing.Returns a grayscale image.
        success, image = self.video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_frame_col(self):
        #Camera input for processing.Returns a color image.
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def detect_faces(self):
        #Camera input for processing.Returns color image with face detection.
        ret, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 45 and conf <= 85:
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (180, 255, 10) #BGR
                stroke = 2 #Thickness
                end_cord_x = x + w
                end_cord_y = y + h
            cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
