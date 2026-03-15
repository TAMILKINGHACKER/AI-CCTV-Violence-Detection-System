# AI CCTV Violence Detection System

An AI-powered real-time surveillance system that detects violence and dangerous objects using computer vision techniques. The system uses a live camera feed to monitor human activities and automatically triggers alerts when suspicious behavior or dangerous objects are detected.

This project is designed as a smart security monitoring solution for environments such as campuses, offices, public places, and surveillance systems.

---

# Project Overview

The system continuously monitors a live camera feed and performs the following tasks:

- Detects people and objects in real time.
- Identifies violent interactions between people based on movement and proximity.
- Detects dangerous objects such as knives or scissors.
- Saves evidence screenshots automatically.
- Sends instant alerts via Telegram when a threat is detected.

The project combines computer vision, machine learning, and automation to create a smart CCTV monitoring solution.

---

# Key Features

## Real-Time Object Detection
The system detects multiple objects in a live video stream including:

- Person
- Bottle
- Cell phone
- Chair
- Laptop
- Backpack
- Knife
- Scissors
- Baseball bat
- and many other objects.

The detection is powered by the YOLOv8 deep learning model.

---

## Violence Detection

The system detects violence by analyzing:

- Distance between people
- Motion intensity
- Human interaction patterns

If two or more people are very close and sudden motion occurs, the system classifies it as potential violence.

---

## Dangerous Object Detection

The system highlights dangerous objects such as:

- Knife
- Scissors
- Baseball bat
- Bottle

When such objects appear in the camera view, the system shows a warning message.

---

## Automated Alerts

When a threat is detected the system will:

- Capture a screenshot
- Save it as evidence
- Send an alert message to Telegram
- Play an alarm sound

This enables real-time monitoring and response.

---

# Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Core programming language |
| OpenCV | Video processing and camera handling |
| YOLOv8 | Object detection model |
| NumPy | Mathematical operations |
| Telegram Bot API | Real-time alert notification |
| Ultralytics | Implementation of YOLOv8 |

---

# System Architecture

```
Live Camera Feed
        │
        ▼
Object Detection (YOLOv8)
        │
        ▼
People Detection
        │
        ▼
Motion Analysis
        │
        ▼
Violence Detection
        │
        ▼
Dangerous Object Detection
        │
        ▼
Alert System
        │
        ▼
Screenshot + Telegram Notification
```

---

# Project Folder Structure

```
AI-CCTV-Violence-Detection-System
│
├── main.py
├── detection.py
├── alert_system.py
├── config.py
├── utils.py
├── requirements.txt
├── README.md
│
├── evidence
│   └── (saved screenshots)
│
├── logs
│   └── incidents.log
```

---

# Installation Guide

## Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-CCTV-Violence-Detection-System.git
```

## Step 2: Navigate to the project directory

```bash
cd AI-CCTV-Violence-Detection-System
```

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Start the system using:

```bash
py -3.11 main.py
```

The program will start the camera and begin monitoring the environment.

---

# Example Output

The system interface displays:

```
People: 2
Objects: 6
Threat Level: HIGH

⚠ DANGEROUS OBJECT DETECTED
⚠ VIOLENCE DETECTED
```

When a threat is detected:

- Screenshot is saved in the evidence folder
- Alert is sent to Telegram
- Alarm sound is triggered

---

# Telegram Alert Integration

The system sends instant alerts using Telegram.

Steps:

1. Create a bot using BotFather
2. Obtain your Bot Token
3. Get your Chat ID
4. Add them to config.py

Example:

```
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

---

# Example Evidence Screenshot

Screenshots of detected threats are automatically stored:

```
evidence/violence_123456789.jpg
```

These images act as incident evidence.

---

# Possible Applications

This system can be used for:

- Smart CCTV surveillance
- Campus security
- Public place monitoring
- Workplace safety
- Automated threat detection

---

# Future Improvements

Possible improvements for this project include:

- Person tracking using DeepSORT
- Multi-camera monitoring dashboard
- Video clip recording of incidents
- Cloud-based alert system
- Weapon-specific detection models

---

# Author

Krishnamoorthy G  
B.E Computer Science and Engineering (Cyber Security)
Cyber Security Researcher

---

# License

This project is open source and available for educational and research purposes.
