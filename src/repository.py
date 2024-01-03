from typing import List
from core.process_images import process_images
from data_models.face_data_model import FaceDataModel
from data_models.faces_from_csv import faces_from_csv
from data_models.faces_to_csv import update_face
from data_models.images_from_csv import  images_from_csv
from data_models.images_to_csv import add_images_to_csv, update_image
from data_models.person_data_model import PersonDataModel
from data_models.persons_from_csv import persons_from_csv
from data_models.persons_to_csv import add_persons_to_csv, update_person


class Repository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # Initialize your repository here
        pass

    def get_images(self):
        return images_from_csv()
    
    def get_faces(self):
        return faces_from_csv()


    def add_images(self, images):
        processed_images = process_images(images=images)
        add_images_to_csv(processed_images)
        return self.get_images()
    

    def update_image(self, image_id, image):
        update_image(image_id=image_id, image=image)
        return self.get_images()
        
    
    def get_persons(self):
        return persons_from_csv()
    
    def get_person(self, person_id):
        persons = self.get_persons()
        for person in persons:
            if person.personId == person_id:
                return person
        return None
    
    def add_persons(self, persons_list):
        add_persons_to_csv(persons_list=persons_list)
        return (self.get_persons(), self.get_images())
    
    def update_person(self, person_id, person):
        update_person(person_id=person_id, person=person)
        return (self.get_persons(), self.get_images())
    
    def add_verified_faces_to_person(self, person: PersonDataModel, faces: List[FaceDataModel]):
        for face in faces:
            face.update_verified(True)
            face.update_person_id(person.personId)
            update_face(face_id= face.faceId, face=face)
        return (self.get_persons(), self.get_images())

    def remove_verified_faces(self, person: PersonDataModel, faces):
        for face in faces:
            person.verified_faces.remove(face)
        update_person(person_id= person.personId, person=person )
        return (self.get_persons(), self.get_images())
    
    def update_face(self, face_id, face):
        update_face(face_id= face_id, face=face)
        return (self.get_persons(), self.get_images())
    

