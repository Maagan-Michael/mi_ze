class FaceDataModel:
    def __init__(self,imageId, faceId, faceImagePath, personId, box, face_encoding = None):
        self.faceId = faceId
        self.faceImagePath = faceImagePath
        self.personId = personId
        self.box = box
        self.imageId = imageId
        self.face_encoding = face_encoding

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