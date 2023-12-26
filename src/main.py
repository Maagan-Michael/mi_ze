
import os
from typing import List
import cv2
from core.data_models.face_data_model import FaceDataModel
from core.data_models.image_data_model import ImageDataModel
from core.encode_image_faces import encode_image_faces
from core.show_image_with_faces import show_image_with_faces
from core.yolov8_face import YOLOv8_face
from process_image_faces import process_image_faces

images = [ImageDataModel( image_path=r'images\test3.jpg',image_id="test3"),ImageDataModel( image_path=r'images\test_image.png',image_id="test")]

unknown_images = [ImageDataModel( image_path=r'images\test4.jpg',image_id="test4")]
images_with_faces = []
unknown_images_with_faces = []

# Initialize YOLOv8_face object detector
YOLOv8_face_detector = YOLOv8_face(conf_thres=0.4, iou_thres=0.5)
for image in images:
    faces = process_image_faces(imageData=image, neural_net_model=YOLOv8_face_detector)
    for face in faces:
        image.add_face(face)
    images_with_faces.append(image)

for image in unknown_images:
    faces = process_image_faces(imageData=image, neural_net_model=YOLOv8_face_detector)
    for face in faces:
        image.add_face(face)
    unknown_images_with_faces.append(image)




print("Encoding faces...")
encoded_images = [encode_image_faces(image) for image in images_with_faces]
unknown_encoded_images = [encode_image_faces(image) for image in unknown_images_with_faces]





import face_recognition
known_faces: List[FaceDataModel] = [face for image in encoded_images for face in image.faces]
# known_faces = [face.get_face_encoding() for face in [image.faces for image in encoded_images]]
# Load the unknown face encoding
for image in unknown_encoded_images:
    for face in image.faces:
        unknown_face_encoding = face.get_face_encoding()
        results = face_recognition.compare_faces(known_face_encodings=[face.get_face_encoding() for face in  known_faces],face_encoding_to_check= unknown_face_encoding,tolerance=0.6)
        
        for i in range(len(results)):
            if results[i]:
                known_face = known_faces[i]
                known_face_image_id = known_face.imageId
                
                known_face_image = None
                for img in encoded_images:
                    if img.image_id == known_face_image_id:
                        known_face_image = img
                        break


                print("its a match! unknown face:", face.get_face_id(), "matches known face:", known_face.get_face_id())
                srcimg = cv2.imread(face.get_face_image_path())
                cv2.imshow("image", srcimg)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                srcimg = cv2.imread(known_face.get_face_image_path())
                cv2.imshow("image", srcimg)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
