import os
import cv2
import numpy as np

from core.format_image_yolov5 import format_yolov5
from core.predict_from_model_and_image import predict_from_model_and_image


def extract_people_bodies_from_image(image, model, output_directory):
    img = format_yolov5(image.get_image_path())
    class_ids, confidences, boxes = predict_from_model_and_image(img, model)

    os.makedirs(output_directory, exist_ok=True)

    for i, (classid, confidence, box) in enumerate(zip(class_ids, confidences, boxes)):
        if classid == 0: #meaning only persons
            x, y, w, h = box
            person_image = img[y:y+h, x:x+w]

            output_path = os.path.join(output_directory,  f"{image.get_image_id()}_person_{i}.png")
            cv2.imwrite(output_path, person_image)


