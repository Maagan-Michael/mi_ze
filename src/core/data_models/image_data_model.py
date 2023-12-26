
from typing import List
from core.data_models.face_data_model import FaceDataModel


class ImageDataModel:
    def __init__(self, image_id, image_path, faces: List[FaceDataModel] = None, metadata=None):
        self.image_id = image_id
        self.image_path = image_path
        self.metadata = metadata or {}
        self.faces = faces or []

    def get_image_id(self):
        return self.image_id

    def get_image_path(self):
        return self.image_path
    
    def get_faces(self):
        return self.faces
    
    def get_metadata(self):
        return self.metadata
    
    def add_face(self,face:FaceDataModel):
        self.faces.append(face)

    def update_face(self, face_id, new_face):
        for i, face in enumerate(self.faces):
            if face.get_face_id() == face_id:
                self.faces[i] = new_face
                break
