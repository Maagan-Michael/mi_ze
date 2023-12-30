

import cv2

from core.cut_picture_from_box import cut_picture_from_box
from core.data_models.face_data_model import FaceDataModel
from core.data_models.image_data_model import ImageDataModel



def process_image_faces(imageData:ImageDataModel, neural_net_model):
    srcimg = cv2.imread(imageData.get_image_path())
    # Detect Objects
    boxes, scores, classids, kpts = neural_net_model.detect(srcimg)
    faces = []
    for i, box in enumerate(boxes):
        face_image_file_name = f"{imageData.get_image_id()}_face_{i}.jpg"

    
        face_image_path =  cut_picture_from_box(picture_path=imageData.get_image_path(),box= box, output_dir="images/extracted_faces",file_name=face_image_file_name)
        faceData = FaceDataModel(imageId=imageData.get_image_id(),faceId= f"{imageData.get_image_id()}_face_{i}", faceImagePath= face_image_path, personId= None, box= box)
        faces.append(faceData)

    return faces
