import csv
import json

from src.data_models.person_data_model import PersonDataModel


FACE_ID_INDEX = 0
FACE_IMAGE_ID_INDEX = 1
FACE_IMAGE_PATH_INDEX = 2
BOX_INDEX = 3
FACE_ENCODING_INDEX = 4
FACE_PERSON_ID_INDEX = 5

PERSON_ID_INDEX = 0
NAME_INDEX = 1
VERIFIED_FACES_INDEX = 2

def add_persons_to_csv(persons_list):
    # Ensure that persons_list is not empty
    if not persons_list:
        print("Error: The list of PersonDataModel instances is empty.")
        return

    # Define the CSV file name
    csv_file_name = "persons.csv"

    # Open the CSV file in write mode
    with open(csv_file_name, mode='w', newline='') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write the header row
        # Write each PersonDataModel instance to the CSV file
        for person in persons_list:
            csv_writer.writerow([person.person_id, person.name])

    print(f"Data written to {csv_file_name}")


def update_person(person_id, person: PersonDataModel):
    # Define the CSV file name
    csv_file_name = "persons.csv"

    # Read the existing data from the CSV file
    with open(csv_file_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    # Find the row with the matching person_id
    for i, row in enumerate(rows):
        if row[PERSON_ID_INDEX] == person_id:
            # Update the row with the new data
            rows[i] = [person.person_id, person.name]

    # Write the updated data back to the CSV file
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)


     # Open the faces.csv file in read mode
    with open('faces.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Create a list of all the rows in the CSV file
        rows = list(reader)
        # Find the indices of the rows with the given image_id
        face_indices = [i for i, row in enumerate(rows) if row[FACE_PERSON_ID_INDEX] == person_id]
        # delete the rows at the given indices
        for index in sorted(face_indices, reverse=True):
            print()
            del rows[index]
    
    
    # Open the faces.csv file in write mode
    with open('faces.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for face in person.verified_faces:
            writer.writerow([ face.face_id,face.image_id,  face.face_image_path, json.dumps(face.box), face.face_encoding, face.person_id])
    
