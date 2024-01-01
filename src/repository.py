from core.process_images import process_images
from data_models.images_from_csv import images_from_csv
from data_models.images_to_csv import add_images_to_csv, update_image
from data_models.persons_from_csv import persons_from_csv


class Repository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # Initialize your repository here
        pass

    def get_images(self):
        return images_from_csv()


    def add_images(self, images):
        processed_images = process_images(images=images)
        add_images_to_csv(processed_images)
        return self.get_images()
    

    def update_image(self, image_id, image):
        update_image(image_id=image_id, image=image)
        return self.get_images()
        
    
    def get_persons(self):
        return persons_from_csv()
    
    def add_person(self, person):
        person.add_person_to_csv()
        return self.get_persons()


