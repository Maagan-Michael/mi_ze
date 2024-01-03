class FaceDataModel:
    def __init__(self,imageId, faceId, faceImagePath, personId, box, certainty = 0.0, face_encoding = None, is_verified = False):
        self.faceId = faceId
        self.faceImagePath = faceImagePath
        self.personId = personId
        self.box = box
        self.imageId = imageId
        self.face_encoding = face_encoding
        self.certainty = certainty
        self.is_verified = is_verified
        

    def get_face_id(self):
        return self.faceId
    
    def get_face_encoding(self):
        return self.face_encoding
    
    def get_face_image_path(self):
        return self.faceImagePath
    
    def get_person_id(self):
        return self.personId
    
    def update_person_id(self, personId):
        self.personId = personId
    
    def update_face_encoding(self, face_encoding):
        self.face_encoding = face_encoding
    
    def update_certainty(self, certainty):
        self.certainty = certainty

    def update_verified(self, verified):
        self.is_verified = verified
