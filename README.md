# 🏥 Advanced AI Medical Intelligence Platform

## 📖 Overview

Advanced AI Medical Intelligence Platform is an end-to-end web application that leverages Deep Learning, Explainable AI (Grad-CAM), and Large Language Models (LLMs) to assist in chest X-ray analysis.

The platform classifies chest X-ray images as **Normal** or **Pneumonia** using a fine-tuned EfficientNetB0 model, generates visual explanations through Grad-CAM, and produces AI-assisted clinical summaries using OpenRouter LLM.

The application provides a complete workflow including image upload, prediction, explainability, AI-generated reports, and persistent prediction history through a modern React interface powered by a FastAPI backend.

## 🚀 Features

- 🩻 Upload Chest X-ray images
- 🤖 AI-based Pneumonia Detection using EfficientNetB0
- 🎯 Confidence Score
- 🔥 Grad-CAM Explainability
- 📝 AI Medical Report using Google Gemini
- 📊 Prediction History (SQLite)
- 📱 Responsive React UI
- ⚡ FastAPI REST API

---

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- Axios
- CSS

### Backend
- FastAPI
- TensorFlow / Keras
- SQLAlchemy
- SQLite
- Google Gemini API

### AI & ML
- EfficientNetB0
- Grad-CAM

---

## 🏗️ System Architecture

```text
                    +-----------------------+
                    |      React + Vite     |
                    |   Medical Web Portal  |
                    +-----------+-----------+
                                |
                                |
                        REST API (HTTP)
                                |
               +----------------+----------------+
               |                                 |
      +--------v---------+              +--------v---------+
      |     FastAPI      |              |    SQLite DB     |
      |  Backend Server  |              | Prediction Logs  |
      +--------+---------+              +------------------+
               |
       +-------+--------+
       |                |
+------v------+   +-----v------+
| CNN Model   |   | OpenRouter |
|EfficientNet |   | LLM Report |
+------+------+
       |
+------v------+
| Grad-CAM    |
| Heatmap     |
+-------------+

```


## 📂 Project Structure

```text
Advanced-AI-Medical-Intelligence-Platform/
│
├── backend/
│   │
│   ├── app/
│   │   ├── main.py                                 
│   │   │
│   │   ├── api/
│   │   │   └── history.py
│   │   │   ├── predict.py             
│   │   │   └── report.py         
│   │   │
│   │   ├── services/
│   │   │   ├── ai_service.py  
│   │   │   ├── gradcam_service.py             
│   │   │   └── llm_service.py
│   │   │              
│   │   ├── database/
│   │   │   ├── crud.py  
│   │   │   ├── db.py             
│   │   │   ├── dependencies.py
│   │   │   └── models.py
│   │   │
│   │   └── utils/
│   │     └── image_unitls.py
│   │
│   ├── model/
│   │   └── pneumonia_model.keras   
│   │
│   ├── training/
│   │   └── data_loader.py
│   │   ├── fine_tune_model.py             
│   │   ├── model.py 
│   │   └── train_model.py        
│   │
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   │
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   │
│   │   ├── components/
│   │   │   ├── UploadCard.jsx
│   │   │   ├── PredictionCard.jsx
│   │   │   ├── Navbar.jsx
│   │   │   └── HistoryTable.jsx
│   │   │
│   │   ├── pages/
│   │   │   └── Home.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
│
├── README.md
├── .gitignore
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

```
cd your-repository
```

---

### 2. Backend Setup

```
cd backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

---

### 3. Frontend Setup

```
cd frontend
```

Install packages

```bash
npm install
```

Run

```bash
npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---
## Environment Variables

Create a `.env` file inside the backend directory.

```env
OPENROUTER_API_KEY=your_api_key
```
## 📸 Screenshots

### Home Page

<img width="1899" height="956" alt="image" src="https://github.com/user-attachments/assets/dedf5541-338e-406f-b5f1-c9debe02ad2d" />

### Image Uploading

<img width="1899" height="958" alt="image" src="https://github.com/user-attachments/assets/bb6c82d2-930e-4389-be30-1d5753fd23ef" />

### Prediction Result

<img width="1211" height="645" alt="image" src="https://github.com/user-attachments/assets/9cfa4433-b41a-4237-b187-5ff657dd92e5" />

### AI Medical Report

<img width="1206" height="765" alt="image" src="https://github.com/user-attachments/assets/e97f9bb2-cf13-4ab2-9ac4-27f53bd5de3b" />

<img width="1192" height="824" alt="image" src="https://github.com/user-attachments/assets/8e7299e2-cad5-4d7f-be42-835da655ea10" />

### Grad-CAM Visualization

<img width="1202" height="490" alt="image" src="https://github.com/user-attachments/assets/137d20a4-aa6a-4d97-b139-547faed00033" />


### Prediction History

<img width="1196" height="883" alt="image" src="https://github.com/user-attachments/assets/bdbbb055-22ca-4109-a474-d0ae28d55f1b" />


---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/predict` | Upload image and get prediction |
| GET | `/history` | Fetch prediction history |

---

## 🎯 Workflow

1. Upload a chest X-ray image.
2. AI predicts **Normal** or **Pneumonia**.
3. Confidence score is displayed.
4. Grad-CAM highlights important image regions.
5. Gemini AI generates a medical report.
6. Prediction is stored in SQLite history.

---

## 👨‍💻 Author

**Tharun Kumar**
