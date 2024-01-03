
import csv
import os

from data_models.image_data_model import ImageDataModel

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
        writer.writerow([image_id, image_path, metadata])

    
    # Add faces to faces.csv
    with open('faces.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the faces data to the faces.csv file
        for face in faces:
            writer.writerow([ face.faceId,face.imageId,  face.faceImagePath, face.box, face.face_encoding, face.personId, face.certainty, face.is_verified])


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
        rows[image_index] = [image_id, image.get_image_path(), image.get_metadata()]

    # Open the images.csv file in write mode
    with open('images.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the updated rows to the images.csv file
        writer.writerows(rows)

    # Open the faces.csv file in read mode
    with open('faces.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Create a list of all the rows in the CSV file
        rows = list(reader)
        # Find the indices of the rows with the given image_id
        face_indices = [i for i, row in enumerate(rows) if row[FACE_IMAGE_ID_INDEX] == image_id]
        # delete the rows at the given indices
        for index in sorted(face_indices, reverse=True):
            print(index)
            del rows[index]
    
    
    # Open the faces.csv file in write mode
    with open('faces.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for face in image.faces:
            print(face.faceId)
            writer.writerow([ face.faceId,face.imageId,  face.faceImagePath, face.box, face.face_encoding, face.personId,face.certainty, face.is_verified])
    