class FaceDataModel:
    def __init__(self, faceId, faceImagePath, personId, box):
        self.faceId = faceId
        self.faceImagePath = faceImagePath
        self.personId = personId
        self.box = box


    def update_person_id(self, personId):
        self.personId = personId