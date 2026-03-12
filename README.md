# DrishyaMitra – AI Photo Management System

DrishyaMitra is an AI-powered photo management platform that allows users to upload images and automatically analyze facial attributes such as **age, gender, and emotion** using deep learning models.

The system is built using a **modern full-stack architecture** with containerized deployment using Docker and secure access through Nginx with SSL.

---

## 🚀 Features

* Upload photos through a modern React interface
* AI-powered facial analysis using **DeepFace**
* Automatic detection of:

  * Age
  * Gender
  * Emotion
* Face embedding generation for similarity matching
* Secure HTTPS access via **Nginx Reverse Proxy**
* Containerized deployment with **Docker & Docker Compose**
* Photo gallery with AI metadata
* Scalable backend architecture

---

## 🧠 AI Capabilities

The platform uses **DeepFace**, a deep learning-based facial analysis framework.

AI analysis includes:

* Face detection
* Age estimation
* Gender prediction
* Emotion recognition
* Face embedding generation for similarity detection

---

## 🏗️ System Architecture

User → React Frontend → Nginx Reverse Proxy (SSL) → Flask Backend API → DeepFace AI → SQLite Database

Components:

| Layer            | Technology     |
| ---------------- | -------------- |
| Frontend         | React.js       |
| Backend          | Flask (Python) |
| AI Model         | DeepFace       |
| Reverse Proxy    | Nginx          |
| Containerization | Docker         |
| Database         | SQLite         |
| Security         | SSL (HTTPS)    |

---

## 📂 Project Structure

```
drishyamitra-project/
│
├── backend/
│   ├── app.py
│   ├── photo_routes.py
│   ├── face_service.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   └── uploads/
│
├── frontend/
│   └── React Application
│
├── nginx/
│   └── nginx.conf
│
├── ssl/
│   ├── cert.pem
│   └── key.pem
│
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/drishyamitra-project.git
cd drishyamitra-project
```

---

### 2️⃣ Build and start the project

```
docker compose up --build
```

This will start:

* Frontend container
* Backend container
* Nginx container

---

### 3️⃣ Access the application

Open in browser:

```
https://localhost
```

---

## 📸 Using the Application

1. Open the **Upload** page
2. Select an image
3. Click **Upload Image**
4. AI analysis will automatically run
5. View results in the **Gallery**

Example AI output:

```
Age: 24
Gender: Male
Emotion: Happy
```

---

## 🔐 SSL Configuration

The project uses **self-signed SSL certificates** for secure HTTPS communication.

Certificates are located in:

```
ssl/
```

For production deployment, replace them with **Let's Encrypt certificates**.

---

## 🐳 Docker Services

| Service  | Port     | Description            |
| -------- | -------- | ---------------------- |
| Frontend | 3000     | React application      |
| Backend  | 5000     | Flask API              |
| Nginx    | 80 / 443 | Reverse proxy with SSL |

---

## 🔍 API Endpoints

### Upload Photo

```
POST /upload
```

Uploads an image and performs AI analysis.

---

### List Photos

```
GET /list
```

Returns all uploaded images with analysis metadata.

---

### Access Uploaded Images

```
GET /uploads/<filename>
```

Returns stored images.

---

## 🧪 Technologies Used

* Python
* Flask
* React.js
* DeepFace
* TensorFlow
* Docker
* Docker Compose
* Nginx
* SQLite
* OpenSSL

---

## 🎯 Future Improvements

* Cloud storage integration (AWS S3)
* Multi-user photo libraries
* Object detection for non-human photos
* Kubernetes deployment

---

## 👨‍💻 Author

**Tarang Thakur**

Electronics & Communication Engineering
B.Tech Student

GitHub:
https://github.com/Tarang-Thakur

**Vinay Tomar**

Computer Science Engineering
B.Tech Student

GitHub:
https://github.com/Vinaytomar945


---

## 📜 License

This project is developed for educational and research purposes.
