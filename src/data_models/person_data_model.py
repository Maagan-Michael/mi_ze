from typing import List
from pydantic import BaseModel

from src.data_models.face_data_model import FaceDataModel

class PersonDataModel(BaseModel):
    person_id: str
    name: str
    verified_faces: List[FaceDataModel] = []

    def get_person_id(self) -> str:
        return self.person_id

    def get_name(self) -> str:
        return self.name

    def get_verified_faces(self) -> List[FaceDataModel]:
        return self.verified_faces

    def add_verified_face(self, face: FaceDataModel):
        self.verified_faces.append(face)

    def to_json(self) -> str:
        return self.json()

    @classmethod
    def from_json(cls, json_str: str) -> 'PersonDataModel':
        data = cls.parse_raw(json_str)
        return cls(**data.dict())




# class PersonDataModel:
#     def __init__(self, person_id, name, verified_faces = None):
#         self.person_id = person_id
#         self.name = name
#         self.verified_faces = verified_faces or []

