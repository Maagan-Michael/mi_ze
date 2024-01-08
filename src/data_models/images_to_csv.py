
import csv
import json
import os
from src.data_models.faces_to_csv import update_face_csv

from src.data_models.image_data_model import ImageDataModel

IMAGE_ID_INDEX = 0
IMAGE_PATH_INDEX = 1
METADATA_INDEX = 2

FACE_ID_INDEX = 0
FACE_IMAGE_ID_INDEX = 1
FACE_IMAGE_PATH_INDEX = 2
BOX_INDEX = 3
FACE_ENCODING_INDEX = 4
PERSON_ID_INDEX = 5


def add_image_to_csv(image: ImageDataModel):
    image_id = image.get_image_id()
    image_path = image.get_image_path()
    faces = image.get_faces()
    metadata = image.get_metadata()

    # Open the images.csv file in append mode
    with open('images.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the image data to the images.csv file
        writer.writerow([image_id, image_path, json.dumps(metadata)])

    
    # Add faces to faces.csv
    with open('faces.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the faces data to the faces.csv file
        for face in faces:
            writer.writerow([ face.face_id,face.image_id,  face.face_image_path, json.dumps(face.box), face.face_encoding, face.person_id, face.certainty, face.is_verified])


def add_images_to_csv(images):
        for image in images:
            add_image_to_csv(image)

    
def update_image(image_id, image:ImageDataModel):
    # Open the images.csv file in read mode
    with open('images.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Create a list of all the rows in the CSV file
        rows = list(reader)
        # Find the index of the image with the given image_id
        image_index = [row[IMAGE_ID_INDEX] for row in rows].index(image_id)
        # Update the row at the given index
        rows[image_index] = [image_id, image.get_image_path(), json.dumps(image.metadata)]

    # Open the images.csv file in write mode
    with open('images.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the updated rows to the images.csv file
        writer.writerows(rows)

    # Open the faces.csv file in read mode
    for face in image.faces:
        update_face_csv(face_id= face.face_id, face=face)
