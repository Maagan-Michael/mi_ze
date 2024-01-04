import csv
import json

import numpy as np
from src.data_models.face_data_model import FaceDataModel
from src.data_models.faces_from_csv import faces_from_csv
from src.data_models.image_data_model import ImageDataModel



def images_from_csv():
    faces = faces_from_csv()
    images = []
    with open('images.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            image_id = row[0]
            image_path = row[1]
            metadata = json.loads(row[2])
            image_faces = [face for face in faces if face.image_id == image_id]
            image = ImageDataModel(image_id=image_id, image_path=image_path, metadata=metadata,faces=image_faces)
            images.append(image)

    return images


