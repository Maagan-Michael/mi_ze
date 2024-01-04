
import json
from typing import List

from src.data_models.face_data_model import FaceDataModel

from typing import List, Dict, Any
from pydantic import BaseModel

class ImageDataModel(BaseModel):
    image_id: str
    image_path: str
    metadata: Dict[str, Any] = {}
    faces: List[FaceDataModel] = []

    def get_image_id(self) -> str:
        return self.image_id

    def get_image_path(self) -> str:
        return self.image_path

    def get_faces(self) -> List[FaceDataModel]:
        return self.faces

    def get_metadata(self) -> Dict[str, Any]:
        return self.metadata

    def add_face(self, face: FaceDataModel):
        self.faces.append(face)

    def update_face(self, face_id: str, new_face: FaceDataModel):
        for i, face in enumerate(self.faces):
            if face.get_face_id() == face_id:
                self.faces[i] = new_face
                break

    def to_json(self) -> str:
        return self.json()

    @classmethod
    def from_json(cls, json_str: str) -> 'ImageDataModel':
        data = cls.parse_raw(json_str)
        return cls(**data.dict())



# class ImageDataModel:
#     def __init__(self, image_id, image_path, faces: List[FaceDataModel] = None, metadata=None):
#         self.image_id = image_id
#         self.image_path = image_path
#         self.metadata = metadata or {}
#         self.faces = faces or []

#     def get_image_id(self):
#         return self.image_id

#     def get_image_path(self):
#         return self.image_path

#     def get_faces(self):
#         return self.faces

#     def get_metadata(self):
#         return self.metadata

#     def add_face(self, face: FaceDataModel):
#         self.faces.append(face)

#     def update_face(self, face_id, new_face):
#         for i, face in enumerate(self.faces):
#             if face.get_face_id() == face_id:
#                 self.faces[i] = new_face
#                 break

#     def to_json(self):
#         return json.dumps({
#             'image_id': self.image_id,
#             'image_path': self.image_path,
#             'metadata': self.metadata,
#             'faces': [face.to_json() for face in self.faces]
#         })

#     @classmethod
#     def from_json(cls, json_str):
#         data = json.loads(json_str)
#         image_id = data.get('image_id')
#         image_path = data.get('image_path')
#         metadata = data.get('metadata')
#         faces = [FaceDataModel.from_json(face) for face in data.get('faces', [])]
#         return cls(image_id, image_path, faces, metadata)


