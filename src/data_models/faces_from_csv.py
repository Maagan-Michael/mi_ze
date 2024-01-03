import csv
import numpy as np
from data_models.face_data_model import FaceDataModel


def faces_from_csv():
    faces = []
    with open('faces.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            face_id = row[0]
            image_id = row[1]
            face_image_path = row[2]
            face_box = np.fromstring(row[3][1:-1], sep=' ')
            face_encoding = np.fromstring(row[4][1:-1], sep=' ')
            person_id = row[5] 
            certainty = float(row[6]) 
            is_verified = row[7]
            face = FaceDataModel(faceId=face_id,imageId=image_id, faceImagePath=face_image_path, box=face_box,
                                 face_encoding=face_encoding, personId=person_id,certainty=certainty,is_verified=is_verified)
            faces.append(face)
    return faces