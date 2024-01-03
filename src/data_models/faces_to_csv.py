import csv
from data_models.face_data_model import FaceDataModel

FACE_ID_INDEX = 0
FACE_IMAGE_ID_INDEX = 1
FACE_IMAGE_PATH_INDEX = 2
BOX_INDEX = 3
FACE_ENCODING_INDEX = 4
PERSON_ID_INDEX = 5
CERTAINTY_INDEX = 6
IS_VERIFIED_INDEX = 7

def update_face(face_id, face: FaceDataModel):
    # Define the CSV file name
    csv_file_name = "faces.csv"

    # Read the existing data from the CSV file
    with open(csv_file_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        

    # Find the row with the matching person_id
    for i, row in enumerate(rows):
        if row[FACE_ID_INDEX] == face_id:
            # Update the row with the new data
            rows[i] = [face.faceId, face.imageId, face.faceImagePath, face.box, face.face_encoding, face.personId, face.certainty, face.is_verified]

  
    # Write the updated data back to the CSV file
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)
    
