# 🏥 Advanced AI Medical Intelligence Platform

An AI-powered web application for chest X-ray analysis that detects **Pneumonia** or **Normal** cases using **EfficientNetB0**, generates **Grad-CAM visualizations**, and provides an **AI-generated medical report** using **Google Gemini**.

---

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

## 📸 Screenshots

### Home Page

> Add screenshot here

### Prediction Result

> Add screenshot here

### Grad-CAM Visualization

> Add screenshot here

### Prediction History

> Add screenshot here

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
