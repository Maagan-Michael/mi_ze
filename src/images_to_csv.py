
from core.data_models.image_data_model import ImageDataModel
import csv
import os

def image_to_csv(image: ImageDataModel):
    image_id = image.get_image_id()
    image_path = image.get_image_path()
    faces = image.get_faces()
    metadata = image.get_metadata()

    # Open the images.csv file in append mode
    with open('images.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the image data to the images.csv file
        writer.writerow([image_id, image_path, metadata])

    
    # Add faces to faces.csv
    with open('faces.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the faces data to the faces.csv file
        for face in faces:
            writer.writerow([ face.faceId,face.imageId,  face.faceImagePath, face.box, face.face_encoding, face.personId])


def images_to_csv(images):
        for image in images:
            image_to_csv(image)    