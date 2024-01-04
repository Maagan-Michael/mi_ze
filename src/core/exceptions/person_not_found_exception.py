class PersonNotFoundException(Exception):
    def __init__(self, person_id: str):
        self.person_id = person_id
        super().__init__(f"Person with ID {person_id} not found.")
