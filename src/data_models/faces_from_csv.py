import csv
import numpy as np
from src.data_models.face_data_model import FaceDataModel
import json


def faces_from_csv():
    faces = []
    with open('faces.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            face_id = row[0]
            image_id = row[1]
            face_image_path = row[2]
            face_box = json.loads(row[3])  # Convert string to dictionary
            face_encoding = json.loads(row[4])
            person_id = row[5] 
            certainty = float(row[6]) 
            is_verified = row[7]
            face = FaceDataModel(face_id=face_id,image_id=image_id, face_image_path=face_image_path, box=face_box,
                                 face_encoding=face_encoding, person_id=person_id,certainty=certainty,is_verified=is_verified)
            faces.append(face)
    return faces