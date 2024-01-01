
import os
from typing import List
import cv2
from core.data_models.face_data_model import FaceDataModel
from core.data_models.image_data_model import ImageDataModel
from core.data_models.images_from_csv import images_from_csv
from core.data_models.person_data_model import PersonDataModel
from core.data_models.persons_from_csv import persons_from_csv
from core.get_faces_from_images import get_faces_from_image_data_model





# processed_images = process_images(images=images)
# images_to_csv(processed_images)

processed_images = images_from_csv()
faces: List[FaceDataModel] = get_faces_from_image_data_model(images= processed_images)
people = persons_from_csv(faces=faces)


import face_recognition
from deepface.commons import functions, realtime, distance as dst

people_faces = [(person,face) for person in people for face in person.verified_faces]
# faces = [face.get_face_encoding() for face in [image.faces for image in processed_images]]
# Load the unknown face encoding
for image in processed_images:
    srcimg = cv2.imread(image.get_image_path())
    d = {}
    for face in image.faces:
        x, y, w, h  = face.box
        
        # Draw box on image
        cv2.rectangle(srcimg, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)
        if(len(face.face_encoding) <1):
            continue
        face_encoding = face.get_face_encoding()
        results = []
        for known_face_encoding in [p_f[1].get_face_encoding() for p_f in people_faces]:
            distance = dst.findCosineDistance(known_face_encoding, face_encoding)
            results.append(distance)

        # results = face_recognition.face_distance(face_encodings=[p_f[1].get_face_encoding() for p_f in people_faces],face_to_compare=face_encoding)
        most_similar_face = min(results)

        for i in range(len(results)):
            if results[i] <= most_similar_face and results[i] <= 0.6:
                verified_person_face = people_faces[i][1]
                person =  people_faces[i][0]
                if person.personId not in d or d[person.personId][2] > results[i]:
                    d[person.personId] = (person,face,results[i])
    


                print("its a match! unknown face:", face.get_face_id(), "matches known face:", verified_person_face.get_face_id(), 'with distance:', results[i])
    

        

    for f_p in d.values():
        face = f_p[1]
        person =  f_p[0]
        match_distance = f_p[2]

        x, y, w, h  = face.box
        

        # Add face ID
        cv2.putText(srcimg, person.name , (int(x-50), int(y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 3)
        cv2.putText(srcimg,str(round(match_distance,3)), (int(x), int(y - 30)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)


    cv2.imshow("image", srcimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
               
