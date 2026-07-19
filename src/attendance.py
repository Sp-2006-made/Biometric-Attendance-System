import sys
print(sys.executable)
print(sys.version)
import face_recognition
import cv2
import os
import csv
from datetime import datetime

# -------------------------------
# Load Known Faces
# -------------------------------

KNOWN_FACES_DIR = "known_faces"

known_face_encodings = []
known_face_names = []

print("Loading known faces...")

for filename in os.listdir(KNOWN_FACES_DIR):

    if filename.endswith(".jpg") or filename.endswith(".png"):

        image_path = os.path.join(KNOWN_FACES_DIR, filename)

        image = face_recognition.load_image_file(image_path)

        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_face_encodings.append(encodings[0])
            known_face_names.append(os.path.splitext(filename)[0])

print("Known Faces Loaded Successfully!")

# -------------------------------
# Create Attendance CSV
# -------------------------------

today = datetime.now().strftime("%Y-%m-%d")
csv_file = f"Attendance_{today}.csv"

marked_names = set()

if os.path.exists(csv_file):

    with open(csv_file, "r") as file:

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            if row:
                marked_names.add(row[0])

else:

    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Name", "Date", "Time"])

# -------------------------------
# Start Webcam
# -------------------------------

video = cv2.VideoCapture(0)

print("Camera Started...")
print("Press Q to Quit")

while True:

    ret, frame = video.read()

    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)

    face_encodings = face_recognition.face_encodings(
        rgb,
        face_locations
    )

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = face_recognition.compare_faces(
            known_face_encodings,
            face_encoding
        )

        name = "Unknown"

        face_distances = face_recognition.face_distance(
            known_face_encodings,
            face_encoding
        )

        if len(face_distances) > 0:

            best_match = face_distances.argmin()

            if matches[best_match]:
                name = known_face_names[best_match]

        # Draw Rectangle

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )

        # Display Name

        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

        # Mark Attendance

        if name != "Unknown" and name not in marked_names:

            now = datetime.now()

            with open(csv_file, "a", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    name,
                    now.strftime("%Y-%m-%d"),
                    now.strftime("%H:%M:%S")
                ])

            marked_names.add(name)

            print(f"Attendance Marked for {name}")

    cv2.imshow("Biometric Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()