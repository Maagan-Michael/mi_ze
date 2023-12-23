
class ImageModel:
    def __init__(self, image_id, image_name, image_path):
        self.image_id = image_id
        self.image_name = image_name
        self.image_path = image_path

    def get_image_id(self):
        return self.image_id

    def get_image_name(self):
        return self.image_name

    def get_image_path(self):
        return self.image_path