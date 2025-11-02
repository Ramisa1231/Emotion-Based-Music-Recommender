
import nltk
from transformers import pipeline

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

HF_MODEL = "bhadresh-savani/distilbert-base-uncased-emotion"
_classifier = pipeline("text-classification", model=HF_MODEL, top_k=None)

GOEMO_MAP = {
    "joy": "joy", "love": "joy",
    "surprise": "surprise",
    "anger": "anger",
    "fear": "fear",
    "sadness": "sadness"
}

def detect_emotion(text: str) -> str:
    if not text.strip():
        return "neutral"
    preds = _classifier(text)[0]
    label = max(preds, key=lambda x: x["score"])["label"].lower()
    return GOEMO_MAP.get(label, label)
