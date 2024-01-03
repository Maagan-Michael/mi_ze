from typing import List

from data_models.image_data_model import ImageDataModel



def get_faces_from_image_data_model(images: List[ImageDataModel]):
    return [face for image in images for face in image.faces]