import cv2

from data_models.image_data_model import ImageDataModel
from repository import Repository


def show_image_with_faces(image:ImageDataModel):
    repository = Repository()
    srcimg = cv2.imread(image.get_image_path())
    for face in image.faces:
        x, y, w, h = face.box
        face_id = face.get_face_id() # Get the face ID
        person = repository.get_person(person_id=face.personId)
        cv2.rectangle(srcimg, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)

        if face.certainty is not None and person is not None:
            percentage_string = f"{round(face.certainty*100,1)}%"
            cv2.putText(srcimg, person.name , (int(x-50), int(y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 3)
            cv2.putText(srcimg,percentage_string, (int(x), int(y - 30)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)
        
    cv2.imshow("image", srcimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()