# 🎧 Emotion-Based Music Recommender

An intelligent **Django web application** that detects user emotions using a **pretrained NLP model** (`bhadresh-savani/distilbert-base-uncased-emotion`) and recommends music tracks from **Spotify’s Audio Features dataset** that match the detected emotional state.

---

## 🧠 Overview
This project integrates **Natural Language Processing (NLP)** and **Music Information Retrieval (MIR)** to bridge emotions and music.  
The system interprets user text input (e.g., “I feel peaceful today”) to identify emotional states such as *joy, sadness, anger,* or *love*, and then recommends songs with matching **valence**, **energy**, and **acoustic features** from Spotify.

---

## ⚙️ Features
- 💬 **Emotion Detection:** Uses `bhadresh-savani/distilbert-base-uncased-emotion` fine-tuned on emotion-labelled English text.
- 🎵 **Music Recommendation:** Based on Spotify features (valence, energy, danceability, acousticness, tempo, etc.).
- 📈 **Evaluation Metrics:**
  - 🎭 Emotion Match Score (EMS)
  - 🎲 Diversity Score
  - 💡 Novelty Score
  - ⚖️ Correction Factor (CF)
  - ❤️ Listener Satisfaction Score (LSS)
- 🧮 **Interactive Django UI:** Users enter text and instantly receive recommended songs and evaluation results.
- ☁️ **Colab Deployment:** Fully executable in Google Colab with `ngrok` for public live demos.

---

## 🧩 Tech Stack
| Category | Tools Used |
|-----------|-------------|
| **Frontend** | HTML, CSS (Django Templates), Chart.js |
| **Backend** | Django, Python |
| **ML/NLP** | HuggingFace Transformers (`bhadresh-savani/distilbert-base-uncased-emotion`) |
| **Data** | Spotify Audio Features (Kaggle) |
| **Evaluation** | Scikit-learn, Pandas, Matplotlib |
| **Deployment** | Google Colab + ngrok |

---

## 📊 Example Output

| Metric | Score |
|--------|--------|
| Diversity | 1.00 |
| Novelty | 0.725 |
| Emotion Match | 0.85 |
| Correction Factor | 1.0 |
| **Listener Satisfaction Score (LSS)** | **0.858** |

---

## 🧪 Setup Instructions

### 1. Clone the Repository

%cd /content <br>
!git clone https://github.com/Ramisa1231/Emotion-Based-Music-Recommender.git<br>
%cd Emotion-Based-Music-Recommender

### 2. Create a Virtual Environment

python -m venv env <br>
source env/bin/activate  # Linux/Mac <br>
env\Scripts\activate     # Windows

### 3. Install Dependencies

pip install -r requirements.txt <br>

### 4. Create an account in ngrok
go to https://dashboard.ngrok.com/get-started/setup/windows <br>
click Your Authtoken <br>
Copy your Authtoken

### 5.  Run in Google Colab

!ngrok config add-authtoken paste your token here <br>
from pyngrok import ngrok  <br>
public_url = ngrok.connect(8000).public_url <br>
print("🌍 Public Django URL:", public_url) <br>

### 6. Run Migrations and Start the Server

python manage.py migrate <br>
python manage.py runserver


Once the server starts, open the public url in your browser to interact with the Django app.


