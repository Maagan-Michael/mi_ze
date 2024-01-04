import json
from typing import Dict, Any

import numpy as np
class FaceDataModel:
    def __init__(self, imageId: str, faceId: str, faceImagePath: str, personId: str, box: Dict[str, int], certainty: float = 0.0, face_encoding: Any = None, is_verified: bool = False):
        self.faceId = faceId
        self.faceImagePath = faceImagePath
        self.personId = personId
        self.box = box
        self.imageId = imageId
        self.face_encoding = face_encoding
        self.certainty = certainty
        self.is_verified = is_verified

    def get_face_id(self) -> str:
        return self.faceId

    def get_face_encoding(self) -> Any:
        return self.face_encoding

    def get_face_image_path(self) -> str:
        return self.faceImagePath

    def get_person_id(self) -> str:
        return self.personId

    def update_person_id(self, personId: str):
        self.personId = personId

    def update_face_encoding(self, face_encoding: Any):
        self.face_encoding = face_encoding

    def update_certainty(self, certainty: float):
        self.certainty = certainty

    def update_verified(self, verified: bool):
        self.is_verified = verified

    def to_json(self) -> str:
        return json.dumps({
            'faceId': self.faceId,
            'faceImagePath': self.faceImagePath,
            'personId': self.personId,
            'box': self.box.tolist(),
            'imageId': self.imageId,
            'face_encoding': self.face_encoding.tolist(),
            'certainty': self.certainty,
            'is_verified': self.is_verified
        })

    @classmethod
    def from_json(cls, json_str: str) -> 'FaceDataModel':
        data = json.loads(json_str)
        return cls(
            data['imageId'],
            data['faceId'],
            data['faceImagePath'],
            data['personId'],
            np.array(data['box']),
            data['certainty'],
            np.array(data['face_encoding']),
            data['is_verified']
        )
