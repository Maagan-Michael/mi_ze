from typing import List
import cv2
from deepface.commons import functions, realtime, distance as dst
from src.core.calculate_probability_of_face_to_person import calculate_probability_of_face_to_person
from src.data_models.face_data_model import FaceDataModel
from src.data_models.image_data_model import ImageDataModel
from src.data_models.person_data_model import PersonDataModel
from src.data_models.persons_from_csv import persons_from_csv

TRESHOLD = dst.findThreshold("Facenet512", "cosine") + 0.4

def face_predictions_on_image(image: ImageDataModel,persons: List[PersonDataModel]):

    
    persons_faces = [(person,face) for person in persons for face in person.verified_faces]
    
    d = {}
    for face in image.faces:
        if(len(face.face_encoding) <1):
            print("no face encoding")
            continue
        face_encoding = face.get_face_encoding()
        results = []
        for known_face_encoding in [p_f[1].get_face_encoding() for p_f in persons_faces]:
            distance = dst.findCosineDistance(known_face_encoding, face_encoding)
            results.append(distance)

        # results = face_recognition.face_distance(face_encodings=[p_f[1].get_face_encoding() for p_f in persons_faces],face_to_compare=face_encoding)
        most_similar_face = min(results)

        for i in range(len(results)):
            if results[i] <= most_similar_face and results[i] <= TRESHOLD:
                verified_person_face = persons_faces[i][1]
                person =  persons_faces[i][0]
                if person.person_id not in d or d[person.person_id][2] > results[i]:
                    probability = calculate_probability_of_face_to_person(person=person,face=face)
                    d[person.person_id] = (person,face,probability)
    


                print("its a match! unknown face:", face.get_face_id(), "matches known face:", verified_person_face.get_face_id(), 'with distance:', results[i])
    

    for f_p in d.values():
        face: FaceDataModel = f_p[1]
        person =  f_p[0]
        match_probability = f_p[2]
        if match_probability < 0.4:
            continue

        face.update_person_id(person_id=person.person_id)
        face.update_certainty(match_probability)


        
        image.update_face(face_id=face.face_id, new_face=face)





    return image