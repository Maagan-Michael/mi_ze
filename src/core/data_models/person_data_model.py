class PersonDataModel:
    def __init__(self, personId, name, faces = None):
        self.personId = personId
        self.name = name
        self.faces = faces or []

