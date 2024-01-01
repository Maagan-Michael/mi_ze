class PersonDataModel:
    def __init__(self, personId, name, verified_faces = None):
        self.personId = personId
        self.name = name
        self.verified_faces = verified_faces or []

