
import os
from typing import List
import cv2
from core.data_models.face_data_model import FaceDataModel
from core.data_models.image_data_model import ImageDataModel
from core.data_models.person_data_model import PersonDataModel

from core.yolov8_face import YOLOv8_face
import csv
from images_from_csv import images_from_csv
from images_to_csv import images_to_csv

from process_images import process_images

images = [ImageDataModel( image_path=r'images\test3.jpg',image_id="test3"),ImageDataModel( image_path=r'images\test_image.png',image_id="test"),ImageDataModel( image_path=r'images\test4.jpg',image_id="test4"),ImageDataModel( image_path=r'images\test_image2.jpeg',image_id="test2"), ImageDataModel( image_path=r'images\test5.jpg',image_id="test5"), ImageDataModel( image_path=r'images\test6.jpg',image_id="test6"), ImageDataModel( image_path=r'images\test7.jpg',image_id="test7"), ImageDataModel( image_path=r'images\test8.jpg',image_id="test8"), ImageDataModel( image_path=r'images\test9.jpg',image_id="test9"), ImageDataModel( image_path=r'images\test10.jpg',image_id="test10"), ImageDataModel( image_path=r'images\test11.jpg',image_id="test11"), ImageDataModel( image_path=r'images\test12.jpg',image_id="test12"), ImageDataModel( image_path=r'images\test13.jpg',image_id="test13"), ImageDataModel( image_path=r'images\test14.jpg',image_id="test14"), ImageDataModel( image_path=r'images\test15.jpg',image_id="test15"), ImageDataModel( image_path=r'images\test16.jpg',image_id="test16"), ImageDataModel( image_path=r'images\test17.jpg',image_id="test17"), ImageDataModel( image_path=r'images\test18.jpg',image_id="test18"), ImageDataModel( image_path=r'images\test19.jpg',image_id="test19"), ImageDataModel( image_path=r'images\test20.jpg',image_id="test20"), ImageDataModel( image_path=r'images\test21.jpg',image_id="test21"), ImageDataModel( image_path=r'images\test22.jpg',image_id="test22"), ImageDataModel( image_path=r'images\test23.jpg',image_id="test23"), ]
# images = [ImageDataModel( image_path=r'images\test3.jpg',image_id="test3"),ImageDataModel( image_path=r'images\test_image.png',image_id="test")]



# Initialize YOLOv8_face object detector
# YOLOv8_face_detector = YOLOv8_face(conf_thres=0.4, iou_thres=0.5)
# known_processed_images = process_images(images=images, neural_net_model=YOLOv8_face_detector)

# images_to_csv(known_processed_images)

processed_images = images_from_csv()
for image in processed_images:
    for face in image.faces:
        print(face.get_face_id())
        if len(face.face_encoding) == 0 :
            srcimg = cv2.imread(face.get_face_image_path())
            cv2.imshow("image", srcimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()





# import face_recognition
# known_faces: List[FaceDataModel] = [face for image in known_processed_images for face in image.faces]
# # known_faces = [face.get_face_encoding() for face in [image.faces for image in processed_images]]
# # Load the unknown face encoding
# for image in unknown_processed_images:
#     for face in image.faces:
#         unknown_face_encoding = face.get_face_encoding()
#         results = face_recognition.face_distance(face_encodings=[face.get_face_encoding() for face in  known_faces],face_to_compare=unknown_face_encoding)
#         most_similar_face = min(results)
#         for i in range(len(results)):
#             if results[i] <= most_similar_face and results[i] <= 0.6:
#                 known_face = known_faces[i]
#                 known_face_image_id = known_face.imageId
                
#                 known_face_image = None
#                 for img in known_processed_images:
#                     if img.image_id == known_face_image_id:
#                         known_face_image = img
#                         break


#                 print("its a match! unknown face:", face.get_face_id(), "matches known face:", known_face.get_face_id(), 'with distance:', results[i])
#                 srcimg = cv2.imread(face.get_face_image_path())
#                 cv2.imshow("image", srcimg)
#                 cv2.waitKey(0)
#                 cv2.destroyAllWindows()
#                 srcimg = cv2.imread(known_face.get_face_image_path())
#                 cv2.imshow("image", srcimg)
#                 cv2.waitKey(0)
#                 cv2.destroyAllWindows()
