from typing import List
from core.data_models.image_data_model import ImageDataModel
from core.encode_image_faces import encode_image_faces
from core.process_image_faces import process_image_faces


def process_images(images: List[ImageDataModel], neural_net_model):
    images_with_faces = []
    for image in images:
        faces = process_image_faces(imageData=image, neural_net_model=neural_net_model)
        for face in faces:
            image.add_face(face)
        images_with_faces.append(image)
    

    processed_images =[encode_image_faces(image) for image in images_with_faces]
    
    return processed_images