from typing import List
from deepface import DeepFace
import numpy as np
from src.core.cut_picture_from_box import cut_picture_from_box
from src.data_models.face_data_model import FaceDataModel
from src.data_models.image_data_model import ImageDataModel



def process_images(images: List[ImageDataModel]):
    images_with_faces = []
    
    for image in images:
        print(image.image_id)
        image_path = image.get_image_path()
        face_dicts =  DeepFace.represent(img_path=image_path, model_name="Facenet512",detector_backend="retinaface",enforce_detection=False)
        for i,d in enumerate(face_dicts):
            face_image_file_name = f"{image.get_image_id()}_face_{i}.jpg"
            encoding = d["embedding"]
            box = d["facial_area"]
            face_image_path =  cut_picture_from_box(picture_path=image_path,box= box, output_dir="images/extracted_faces",file_name=face_image_file_name)

            face = FaceDataModel(image_id=image.get_image_id(),face_id= f"{image.get_image_id()}_face_{i}", face_image_path= face_image_path, person_id= "unknown", box= box,face_encoding=encoding)
            image.add_face(face)
        images_with_faces.append(image)

    return images_with_faces
    


