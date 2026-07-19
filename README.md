# Biometric Attendance System using Face Recognition

## Overview

This project is a Python-based biometric attendance system that uses face recognition to identify registered users through a webcam and automatically records their attendance with the current date and time in a CSV file.

## Features

- Real-time face detection using webcam
- Face recognition using stored face images
- Automatic attendance recording
- CSV-based attendance logging
- Simple and easy-to-use implementation

## Technologies Used

- Python
- OpenCV
- face_recognition
- NumPy
- Pandas

## Project Structure

```
Biometric-Attendance-System/
│
├── src/
│   └── attendance.py
├── known_faces/
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Place one or more face images inside the `known_faces` folder.
2. Rename each image using the person's name (e.g., `John.png`).
3. Run the program:

```bash
python src/attendance.py
```

4. The webcam will open.
5. When a registered face is detected, attendance will be recorded automatically in a CSV file.

## Output

The program generates a CSV file containing:

- Name
- Date
- Time

## Future Improvements

- Database integration (SQLite/MySQL)
- Raspberry Pi deployment
- Fingerprint authentication
- Web-based dashboard
- Cloud-based attendance storage
- Multiple camera support

## License

This project is licensed under the MIT License.

## Author

**Sheik Parvezh**