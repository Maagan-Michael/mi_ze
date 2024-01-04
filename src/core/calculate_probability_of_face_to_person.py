import numpy as np
from src.data_models.face_data_model import FaceDataModel
from src.data_models.person_data_model import PersonDataModel
from deepface.commons import functions, realtime, distance as dst

def calculate_probability_of_face_to_person(person: PersonDataModel,face:FaceDataModel):
    penalty = 0.0

    # Check if the number of verified images is less than 2
    if len(person.verified_faces) < 4:
        penalty += (4-len(person.verified_faces)) * 0.02
        if len(person.verified_faces) == 1:
            penalty += 0.05
        


    distances = []
    for verified_face in person.verified_faces:
        # Calculate the distance between the verified image and the unknown image
        if len(verified_face.face_encoding) <1:
            # distances.append(0.4)
            continue
        distance = dst.findCosineDistance(face.face_encoding, verified_face.face_encoding)

        # Add the distance to the list of distances
        distances.append(distance)

    # Calculate the average distance between the verified images
    avg_distance = np.mean(distances)

    # Calculate the probability based on the distances and average distance
    probability = 1 - avg_distance - penalty

    return probability