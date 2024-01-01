import csv


def persons_to_csv(persons_list):
    # Ensure that persons_list is not empty
    if not persons_list:
        print("Error: The list of PersonDataModel instances is empty.")
        return

    # Define the CSV file name
    csv_file_name = "persons.csv"

    # Open the CSV file in write mode
    with open(csv_file_name, mode='w', newline='') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write the header row
        # Write each PersonDataModel instance to the CSV file
        for person in persons_list:
            csv_writer.writerow([person.personId, person.name, ', '.join([face.faceId for face in person.verified_faces])])

    print(f"Data written to {csv_file_name}")
