import csv
from typing import List

from src.data_models.face_data_model import FaceDataModel
from src.data_models.faces_from_csv import faces_from_csv
from src.data_models.person_data_model import PersonDataModel



def persons_from_csv():
    persons_list = []
    faces: List[FaceDataModel] = faces_from_csv()
    csv_file_name="persons.csv"
    # Open the CSV file in read mode
    with open(csv_file_name, mode='r') as csv_file:
        # Create a CSV reader
        csv_reader = csv.reader(csv_file)


        # Find the indices of columns in the header
        person_id_index = 0
        name_index = 1
        verified_faces_index = 2

        # Read each row and create PersonDataModel instances
        for row in csv_reader:
            person_id = row[person_id_index]
            name = row[name_index]
            verified_faces = [face for face in faces if str(face.person_id) == str(person_id) and( face.certainty > 0.6 or face.is_verified) ]
            person_instance = PersonDataModel(person_id=person_id, name=name, verified_faces=verified_faces)
            persons_list.append(person_instance)

   
    return persons_list