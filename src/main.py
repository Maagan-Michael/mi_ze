
import os
from typing import List
import cv2
from core.data_models.face_data_model import FaceDataModel
from core.data_models.image_data_model import ImageDataModel
from core.data_models.images_from_csv import images_from_csv
from core.data_models.person_data_model import PersonDataModel
from core.data_models.persons_from_csv import persons_from_csv
from core.data_models.persons_to_csv import persons_to_csv
from core.process_images import process_images

import csv



images = [ImageDataModel( image_path=r'images\test3.jpg',image_id="test3"),ImageDataModel( image_path=r'images\test_image.png',image_id="test"),ImageDataModel( image_path=r'images\test4.jpg',image_id="test4"),ImageDataModel( image_path=r'images\test_image2.jpeg',image_id="test2"), ImageDataModel( image_path=r'images\test5.jpg',image_id="test5"), ImageDataModel( image_path=r'images\test6.jpg',image_id="test6"), ImageDataModel( image_path=r'images\test7.jpg',image_id="test7"), ImageDataModel( image_path=r'images\test8.jpg',image_id="test8"), ImageDataModel( image_path=r'images\test9.jpg',image_id="test9"), ImageDataModel( image_path=r'images\test10.jpg',image_id="test10"), ImageDataModel( image_path=r'images\test11.jpg',image_id="test11"), ImageDataModel( image_path=r'images\test12.jpg',image_id="test12"), ImageDataModel( image_path=r'images\test13.jpg',image_id="test13"), ImageDataModel( image_path=r'images\test14.jpg',image_id="test14"), ImageDataModel( image_path=r'images\test15.jpg',image_id="test15"), ImageDataModel( image_path=r'images\test16.jpg',image_id="test16"), ImageDataModel( image_path=r'images\test17.jpg',image_id="test17"), ImageDataModel( image_path=r'images\test18.jpg',image_id="test18"), ImageDataModel( image_path=r'images\test19.jpg',image_id="test19"), ImageDataModel( image_path=r'images\test20.jpg',image_id="test20"), ImageDataModel( image_path=r'images\test21.jpg',image_id="test21"), ImageDataModel( image_path=r'images\test22.jpg',image_id="test22"), ImageDataModel( image_path=r'images\test23.jpg',image_id="test23"), ]




# processed_images = process_images(images=images)
# images_to_csv(processed_images)
processed_images = images_from_csv()
# kami_faces = [face for image in processed_images for face in image.faces if face.faceId == "test3_face_5"] 
# omri_faces = [face for image in processed_images for face in image.faces if face.faceId == "test3_face_4"  ]
# yaron_faces = [face for image in processed_images for face in image.faces if face.faceId == "test3_face_3" ]
# amit_faces = [face for image in processed_images for face in image.faces if face.faceId == "test3_face_2" ]
# tzur_faces = [face for image in processed_images for face in image.faces if face.faceId == "test3_face_0" ]
# yonatan_faces = [face for image in processed_images for face in image.faces if face.faceId == "test3_face_7" ]
# alon_faces = [face for image in processed_images for face in image.faces if face.faceId == "test3_face_6" ]
# ofira_faces = [face for image in processed_images for face in image.faces if face.faceId == "test3_face_1" ]
# people = [ PersonDataModel(name='Kami Tazyig',personId="2",verified_faces=kami_faces), PersonDataModel(name='Omri Berchman',personId="1",verified_faces=omri_faces),PersonDataModel(name='Yaron Shaharabani',personId="3",verified_faces=yaron_faces), PersonDataModel(name='Amit Inbar',personId="4",verified_faces=amit_faces), PersonDataModel(name='Tzur Levi',personId="5",verified_faces=tzur_faces), PersonDataModel(name='Yonatan Almog',personId="6",verified_faces=yonatan_faces), PersonDataModel(name='Alon Segal',personId="7",verified_faces=alon_faces), PersonDataModel(name='Ofira Sarid',personId="8",verified_faces=ofira_faces) ]
# persons_to_csv(people)
known_faces: List[FaceDataModel] = [face for image in processed_images for face in image.faces]
people = persons_from_csv(faces=known_faces)
import face_recognition
from deepface.commons import functions, realtime, distance as dst

people_faces = [(person,face) for person in people for face in person.verified_faces]
# known_faces = [face.get_face_encoding() for face in [image.faces for image in processed_images]]
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
        
               
