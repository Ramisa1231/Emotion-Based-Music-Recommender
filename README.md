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
```bash
git clone https://github.com/Ramisa1231/Emotion-Based-Music-Recommender.git
cd Emotion-Based-Music-Recommender

### 2. Create a Virtual Environment

python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run Migrations and Start the Server

python manage.py migrate
python manage.py runserver

### 5. (Optional) Run in Google Colab

from pyngrok import ngrok
ngrok.connect(8000)

Once it prints your public URL, open it in your browser to interact with the Django app.


