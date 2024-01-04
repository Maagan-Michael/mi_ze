
import os
from typing import List
import cv2
from core.get_faces_from_images import get_faces_from_image_data_model
from core.process_images import process_images
from core.show_image_with_faces import show_image_with_faces
from data_models.face_data_model import FaceDataModel
from data_models.face_predictions_on_image import face_predictions_on_image
from data_models.image_data_model import ImageDataModel
from data_models.images_from_csv import images_from_csv
from data_models.person_data_model import PersonDataModel
from data_models.persons_from_csv import persons_from_csv
from repository import Repository
from fastapi import FastAPI
from typing import List
from data_models.face_data_model import FaceDataModel
from data_models.person_data_model import PersonDataModel
from repository import Repository




app = FastAPI()
repository = Repository()

@app.get("/")
def read_root():
    return {"mi": "ze"}

@app.get("/images")
def get_images():
    images = repository.get_images()
    json_images = [image.to_json() for image in images]
    return json_images

@app.post("/images")
def add_images(images):
    return repository.add_images(images)

@app.put("/images/{image_id}")
def update_image(image_id, image):
    return repository.update_image(image_id, image)

@app.get("/faces")
def get_faces():
    return repository.get_faces()

@app.get("/persons")
def get_persons():
    return repository.get_persons()

@app.get("/persons/{person_id}")
def get_person(person_id):
    return repository.get_person(person_id)

@app.post("/persons")
def add_persons(persons_list):
    return repository.add_persons(persons_list)

@app.put("/persons/{person_id}")
def update_person(person_id, person):
    return repository.update_person(person_id, person)

@app.post("/persons/{person_id}/verified_faces")
def add_verified_faces_to_person(person_id, faces):
    person = repository.get_person(person_id)
    return repository.add_verified_faces_to_person(person, faces)

@app.delete("/persons/{person_id}/verified_faces")
def remove_verified_faces(person_id, faces):
    person = repository.get_person(person_id)
    return repository.remove_verified_faces(person, faces)

@app.put("/faces/{face_id}")
def update_face(face_id, face):
    return repository.update_face(face_id, face)























# processed_images = repository.get_images()
# people = repository.get_persons()
# faces:List[FaceDataModel] = repository.get_faces()




# for image in processed_images:
#     image = face_predictions_on_image(image=image, persons=people)
#     show_image_with_faces(image=image)
#     for face in image.faces:
#         if face.certainty > 0.4:
#             repository.update_face(face_id=face.faceId, face=face)
   
        
        





#dummy data
            
# images = [ImageDataModel( image_path=r'images\test3.jpg',image_id="test3"),ImageDataModel( image_path=r'images\test_image.png',image_id="test"),ImageDataModel( image_path=r'images\test4.jpg',image_id="test4"),ImageDataModel( image_path=r'images\test_image2.jpeg',image_id="test2"), ImageDataModel( image_path=r'images\test5.jpg',image_id="test5"), ImageDataModel( image_path=r'images\test6.jpg',image_id="test6"), ImageDataModel( image_path=r'images\test7.jpg',image_id="test7"), ImageDataModel( image_path=r'images\test8.jpg',image_id="test8"), ImageDataModel( image_path=r'images\test9.jpg',image_id="test9"), ImageDataModel( image_path=r'images\test10.jpg',image_id="test10"), ImageDataModel( image_path=r'images\test11.jpg',image_id="test11"), ImageDataModel( image_path=r'images\test12.jpg',image_id="test12"), ImageDataModel( image_path=r'images\test13.jpg',image_id="test13"), ImageDataModel( image_path=r'images\test14.jpg',image_id="test14"), ImageDataModel( image_path=r'images\test15.jpg',image_id="test15"), ImageDataModel( image_path=r'images\test16.jpg',image_id="test16"), ImageDataModel( image_path=r'images\test17.jpg',image_id="test17"), ImageDataModel( image_path=r'images\test18.jpg',image_id="test18"), ImageDataModel( image_path=r'images\test19.jpg',image_id="test19"), ImageDataModel( image_path=r'images\test20.jpg',image_id="test20"), ImageDataModel( image_path=r'images\test21.jpg',image_id="test21"), ImageDataModel( image_path=r'images\test22.jpg',image_id="test22"), ImageDataModel( image_path=r'images\test23.jpg',image_id="test23"), ]
# processed_images = repository.add_images(images=images)
# people = [ PersonDataModel(name='Kami Tazyig',personId="2"), PersonDataModel(name='Omri Berchman',personId="1"),PersonDataModel(name='Yaron Shaharabani',personId="3"), PersonDataModel(name='Amit Inbar',personId="4")]
# repository.add_persons(persons_list=people)

# people = repository.get_persons()
# faces = repository.get_faces()
# kami_faces = [face for face in faces if face.faceId == "test3_face_5"] 
# omri_faces = [face for face in faces if face.faceId == "test3_face_4"  ]
# yaron_faces = [face for face in faces if face.faceId == "test3_face_3" ]
# amit_faces = [face for face in faces if face.faceId == "test3_face_2" ]
# repository.add_verified_faces_to_person(person=people[0], faces=kami_faces)
# repository.add_verified_faces_to_person(person=people[1], faces=omri_faces)
# repository.add_verified_faces_to_person(person=people[2], faces=yaron_faces)
# repository.add_verified_faces_to_person(person=people[3], faces=amit_faces)