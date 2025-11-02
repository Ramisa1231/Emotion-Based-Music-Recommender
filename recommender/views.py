
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from recommender.utils.emotion_detector import detect_emotion
from recommender.utils.recommender import recommend
from recommender.utils.metrics import (
    diversity_score,
    novelty_score,
    emotion_match_score,
    correction_factor,
)

# Example user profile (later, load per-user)
USER_PROFILE = {
    "prefers_uplifting": True,
    "avoids_sad": True,
    "novelty_seeking": False,
}

def home(request):
    """
    Renders a form:
      - POST: takes text input, detects emotion, recommends songs, and computes metrics
      - GET:   renders the empty form
    """
    context = {}
    if request.method == "POST":
        text = request.POST.get("journal_text", "").strip()
        if text:
            # 1) Detect emotion
            emotion = detect_emotion(text)

            # 2) Recommend songs
            recs = recommend(emotion, k=5)  # returns a DataFrame

            # 3) Compute metrics
            diversity = diversity_score(recs)
            novelty = novelty_score(recs)
            match = emotion_match_score(recs, emotion)
            cf = correction_factor(USER_PROFILE, recs)
            lss = round((diversity + novelty + match) / 3 * cf, 3)

            # 4) Build context for template
            context.update({
                "input_text": text,
                "emotion": emotion,
                "recommendations": recs.to_dict(orient="records"),
                "diversity": round(diversity, 3),
                "novelty": round(novelty, 3),
                "match": round(match, 3),
                "correction": cf,
                "lss": lss,
            })
        else:
            context["error"] = "Please enter some text."

    return render(request, "home.html", context)
