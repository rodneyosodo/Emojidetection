import os
from PIL import Image
import numpy as np
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Human_data")

recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_labels = []
x_train = []

def create_test_data(path):
    for p in os.listdir(path):
        new= os.path.join(path, p)
        category = p.split("_")[0]
        for img in os.listdir(new):
            img_array = cv2.imread(os.path.join(new, img), cv2.IMREAD_GRAYSCALE)
            new_img_array = cv2.resize(img_array, dsize=(1632, 1224))
            image_array = np.array(new_img_array, "uint8")
            x_train.append(new_img_array)
            y_labels.append(str(category.replace("-", " ").lower()))

def main():
	create_test_data(image_dir)
	with open("labels.pkl", "wb") as f:
		pickle.dump(label_ids, f)
	recognizer.train(x_train, np.array(y_labels))
	recognizer.save("trainer.yml")

if __name__ == '__main__':
    main()