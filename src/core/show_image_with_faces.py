import cv2

from core.data_models.image_data_model import ImageDataModel

def show_image_with_faces(image:ImageDataModel):
    srcimg = cv2.imread(image.get_image_path())
    for face in image.faces:
        x, y, w, h = face.box
        face_id = face.get_face_id() # Get the face ID
        cv2.rectangle(srcimg, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)
        cv2.putText(srcimg, str(face_id), (int(x), int(y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
    cv2.imshow("image", srcimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()