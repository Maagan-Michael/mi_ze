from core.data_models.image_data_model import ImageDataModel
from core.encode_face import encode_face


def encode_image_faces(image:ImageDataModel):
    for face in image.faces:
        face_image_path = face.get_face_image_path()
        face_encoding = encode_face(face_image_path)
        if face_encoding is not None:
            print("Face encoding:")
            face.update_face_encoding(face_encoding)
        else:
            print("No face found in the image.")
           
    return image

