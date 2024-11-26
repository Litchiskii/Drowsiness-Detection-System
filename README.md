Drowsiness Detection System Using Raspberry Pi
Overview
This project focuses on building a Drowsiness Detection System to reduce accidents caused by driver fatigue. It uses a webcam connected to a Raspberry Pi 4 to monitor facial features in real-time, analyzing the Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR) to detect signs of drowsiness or yawning. Alerts are triggered to warn the driver.

Objectives
Develop a cost-effective and portable drowsiness detection system.
Implement real-time video processing for facial feature analysis.
Detect drowsiness and yawning based on EAR and MAR calculations.
Provide instant alerts to reduce accident risks.
Features
Real-time facial analysis using Python, OpenCV, and dlib.
Affordable and compact system leveraging Raspberry Pi.
Wide application: vehicle safety, workplace monitoring, healthcare.
System Architecture
The system comprises:

Hardware:
Raspberry Pi 4 Model B.
USB webcam.
Micro-USB cable, monitor, and jumper wires.
Software:
Python 3, OpenCV, dlib, NumPy.
Raspberry Pi OS (Debian-based).
Installation
Hardware Setup
Assemble the Raspberry Pi 4 and connect the USB webcam.
Connect the Raspberry Pi to a monitor, keyboard, and mouse for initial setup.
Software Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/Drowsiness-Detection-System.git  
cd Drowsiness-Detection-System  
Install dependencies:
bash
Copy code
pip install -r requirements.txt  
How to Run
Connect the webcam to your Raspberry Pi.
Navigate to the src directory and run the main script:
bash
Copy code
python main.py  
The system will start monitoring for EAR and MAR thresholds, triggering alerts if drowsiness or yawning is detected.
Folder Structure
bash
Copy code
Drowsiness-Detection-System/
│
├── README.md                # Documentation  
├── requirements.txt         # Python dependencies  
├── src/                     # Source code  
│   ├── main.py              # Main detection script  
│   ├── utils.py             # Helper functions  
│   ├── config.py            # Configurations  
│
├── hardware/                # Circuit details  
│   ├── circuit_diagram.png  # Circuit diagrams  
│   ├── connections.txt      # Connection instructions  
│
├── docs/                    # Documentation and reports  
│   ├── report.pdf           # Project report  
│   ├── literature_review.pdf# Literature review  
│
├── data/                    # Sample test files  
│   ├── sample_videos/       # Test video samples  
│   ├── sample_images/       # Test image samples  
└── tests/                   # Unit tests  
Future Enhancements
