
# #encode face
import face_recognition

def encode_face(image_path, times_to_upsample=1 ):
    # Load the image
    image = face_recognition.load_image_file(image_path)

    # Find face locations and encodings
    face_locations = face_recognition.face_locations(image,number_of_times_to_upsample=times_to_upsample, model='cnn')
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Check if at least one face is found
    if len(face_encodings) > 0:
        # Return the face encoding of the first detected face
        return face_encodings[0]
    else:
        if times_to_upsample < 10:
            # Try again with more upsampling
            return encode_face(image_path, times_to_upsample + 1)
        else:
            # Return None if no face is found
            return None