import os
import cv2

def cut_picture_from_box(picture_path, box, output_dir,file_name):
    # Load the picture
    picture = cv2.imread(picture_path)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Cut the picture based on the boxes

    x, y, w, h = box
    cut_picture = picture[int(y):int(y+h), int(x):int(x+w)]

    # Save the cut picture to the output directory
    cut_picture_path = os.path.join(output_dir, file_name)
    cv2.imwrite(cut_picture_path, cut_picture)
    return cut_picture_path
        

