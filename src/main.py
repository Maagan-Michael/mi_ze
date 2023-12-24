
import os
import cv2
from core.data_models.image_data_model import ImageDataModel
from core.yolov8_face import YOLOv8_face
from process_image_faces import process_image_faces

images = [ImageDataModel( image_path=r'images\test3.jpg',image_id="test3"),ImageDataModel( image_path=r'images\test_image2.jpeg',image_id="test2"),ImageDataModel( image_path=r'images\test_image.png',image_id="test")]


images_with_faces = []

# Initialize YOLOv8_face object detector
YOLOv8_face_detector = YOLOv8_face(conf_thres=0.4, iou_thres=0.5)
for image in images:
    faces = process_image_faces(imageData=image, neural_net_model=YOLOv8_face_detector)
    for face in faces:
        image.add_face(face)
    images_with_faces.append(image)

# Show images with boxes
for image_with_faces in images_with_faces:
    image_path = image_with_faces.image_path
    image = cv2.imread(image_path)
    print('final', len(image_with_faces.faces))
    for face in image_with_faces.faces:
        x, y, w, h = face.box
        cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)
    cv2.imshow(image_path, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


