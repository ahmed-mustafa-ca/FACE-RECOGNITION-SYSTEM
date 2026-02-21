# 🧠 Real-Time Face Recognition System

This project is a Deep Learning-powered real-time face recognition system built using Python, OpenCV, and DeepFace. It continuously verifies faces from a live webcam feed against a reference image and displays MATCH or NO MATCH in real time.

---

## 🚀 Features

- Real-time webcam face detection
- Deep learning-based face verification using DeepFace
- Multi-threaded processing for smooth performance
- Thread-safe face verification updates
- Displays MATCH!
- Displays NO MATCH!
- Press Q to exit the application

---

## 🧩 Tech Stack

- Python
- OpenCV
- DeepFace
- Threading (multi-threaded processing)

---

## ⚙️ How It Works

### 1️⃣ Video Capture

The system captures video frames from your webcam. Frames are read continuously for real-time processing.

---

### 2️⃣ Face Verification

Every 30 frames, the system verifies the detected face using DeepFace. Verification runs in a separate thread to prevent lag.

---

### 3️⃣ Multi-Threading Logic

- Verification occurs in a background thread
- A lock ensures safe updates to the faceMatch variable
- Reduces computational bottlenecks and maintains real-time performance

---

### 4️⃣ Real-Time Display

- Shows MATCH! if the live face matches the reference
- Shows NO MATCH! otherwise
- Press Q to quit the application

---

## 🖼️ Setup Reference Image

Place your reference image inside the project folder and name it `reference.jpg`. Update the reference path in your main script if needed.

---

## ⚙️ Requirements

- Python 3.8+
- Webcam
- Good lighting conditions

---

## 📂 Project Structure


├── main.py
├── reference.jpg
├── README.md
├── .gitattributes
├── LICENSE

---

## 🧠 Example Inputs

| Input | Description |
|-------|-------------|
| Webcam Frame | Captured in real-time |
| Reference Image | `reference.jpg` in project folder |
| Frame Interval | Verify every 30 frames |
| Threading | Enabled for smooth performance |

---

## 💻 Example Output

| Output | Description |
|--------|-------------|
| MATCH! | Displayed when detected face matches reference |
| NO MATCH! | Displayed when face does not match |
| Real-Time Video | Frame with overlay text |
| Exit | Press Q to quit application |

---

## 💡 Future Improvements

- Multi-face support
- Display confidence scores
- Support multiple reference images
- GUI using Tkinter or PyQt
- Convert into a security system
- Deploy as a web-based application

---

## 🧑‍💻 Author

Ahmed Mustafa  
Passionate about AI, Deep Learning, and building intelligent systems.

---
