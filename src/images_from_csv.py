import csv

import numpy as np
from core.data_models.face_data_model import FaceDataModel
from core.data_models.image_data_model import ImageDataModel


def images_from_csv():
    faces = faces_from_csv()
    images = []
    with open('images.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            image_id = row[0]
            image_path = row[1]
            metadata = row[2]
            image_faces = [face for face in faces if face.imageId == image_id]
            image = ImageDataModel(image_id=image_id, image_path=image_path, metadata=metadata,faces=image_faces)
            images.append(image)

    return images


def faces_from_csv():
    faces = []
    with open('faces.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            face_id = row[0]
            image_id = row[1]
            face_image_path = row[2]
            face_box = row[3]
            face_encoding = np.fromstring(row[4][1:-1], sep=' ')
            person_id = row[5]
            face = FaceDataModel(faceId=face_id,imageId=image_id, faceImagePath=face_image_path, box=face_box,
                                 face_encoding=face_encoding, personId=person_id)
            faces.append(face)
    return faces