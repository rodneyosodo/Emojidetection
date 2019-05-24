import os
from PIL import Image
import numpy as np
import cv2
import pickle


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Human_data")
recognizer = cv2.face.LBPHFaceRecognizer_create()

def main():
    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []
    path = image_dir
    for p in os.listdir(path):
        new_path= os.path.join(path, p)
        label = p.split("_")[0]
        if not label in label_ids:
            label_ids[label] = current_id
            current_id += 1
        id_ = label_ids[label]
        for img in os.listdir(new_path):
            #img_array = cv2.imread(os.path.join(new, img), cv2.IMREAD_GRAYSCALE)
            #new_img_array = cv2.resize(img_array, dsize=(1632, 1224))
            #image_array = np.array(new_img_array, "uint8")
            pil_image = Image.open(os.path.join(new_path, img)).convert("L")#Convert to gray
            size = (1632, 1224)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, 'uint8')
            x_train.append(image_array)
            y_labels.append(id_)
    with open("Models/labels.pkl", "wb") as f:
        pickle.dump(label_ids, f)
    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("Models/trainer.yml")

if __name__ == '__main__':
    main()

