import json
from typing import Dict, Any

import numpy as np
from pydantic import BaseModel, Field



        
class FaceDataModel(BaseModel):
    image_id: str
    face_id: str
    face_image_path: str
    person_id: str
    box: Dict[str, int]
    certainty: float = 0.0
    face_encoding: list = None
    is_verified: bool = False

    def get_face_id(self) -> str:
        return self.face_id

    def get_face_encoding(self) -> Any:
        return self.face_encoding

    def get_face_image_path(self) -> str:
        return self.face_image_path

    def get_person_id(self) -> str:
        return self.person_id

    def update_person_id(self, person_id: str):
        self.person_id = person_id

    def update_face_encoding(self, face_encoding: Any):
        self.face_encoding = face_encoding

    def update_certainty(self, certainty: float):
        self.certainty = certainty

    def update_verified(self, verified: bool):
        self.is_verified = verified

    def to_json(self) -> str:
        return self.model_dump_json()

    @classmethod
    def from_json(cls, json_str: str) -> 'FaceDataModel':
        data = cls.model_validate_json(json_str)
        return cls(**data.model_dump())
    

    
# class FaceDataModel:
#     def __init__(self, image_id: str, face_id: str, face_image_path: str, person_id: str, box: Dict[str, int], certainty: float = 0.0, face_encoding: Any = None, is_verified: bool = False):
#         self.face_id = face_id
#         self.face_image_path = face_image_path
#         self.person_id = person_id
#         self.box = box
#         self.image_id = image_id
#         self.face_encoding = face_encoding
#         self.certainty = certainty
#         self.is_verified = is_verified

#     def get_face_id(self) -> str:
#         return self.face_id

#     def get_face_encoding(self) -> Any:
#         return self.face_encoding

#     def get_face_image_path(self) -> str:
#         return self.face_image_path

#     def get_person_id(self) -> str:
#         return self.person_id

#     def update_person_id(self, person_id: str):
#         self.person_id = person_id

#     def update_face_encoding(self, face_encoding: Any):
#         self.face_encoding = face_encoding

#     def update_certainty(self, certainty: float):
#         self.certainty = certainty

#     def update_verified(self, verified: bool):
#         self.is_verified = verified

#     def to_json(self) -> str:
#         return json.dumps({
#             'face_id': self.face_id,
#             'face_image_path': self.face_image_path,
#             'person_id': self.person_id,
#             'box': self.box,
#             'image_id': self.image_id,
#             'face_encoding': self.face_encoding.tolist(),
#             'certainty': self.certainty,
#             'is_verified': self.is_verified
#         })

#     @classmethod
#     def from_json(cls, json_str: str) -> 'FaceDataModel':
#         data = json.loads(json_str)
#         return cls(
#             data['image_id'],
#             data['face_id'],
#             data['face_image_path'],
#             data['person_id'],
#             data['box'],
#             data['certainty'],
#             np.array(data['face_encoding']),
#             data['is_verified']
#         )
