
from core.build_yolov5_model import build_yolov5_model
from core.models.image_model import ImageModel
from extract_people_bodies_from_image import extract_people_bodies_from_image

image = ImageModel( image_path=r'images\test_image.png',image_id="1", image_name="test1")
model = build_yolov5_model()

extract_people_bodies_from_image(image, model,'images/extracted_people')