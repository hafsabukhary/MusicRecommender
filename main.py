from textblob import TextBlob
from pygame import mixer
import os
import random

# Define mood mapping based on sentiment scores
mood_mapping = {
    "positive": "happy",
    "negative": "sad",
    # Define more labels and corresponding moods
}

# Get user input (text or voice)
user_input = input("Enter your mood: ")

# Perform sentiment analysis on user input using TextBlob
sentiment = TextBlob(user_input).sentiment
predicted_mood = "happy" if sentiment.polarity > 0 else "sad"  # Simplified logic

# Recommend tracks from local music library based on predicted mood
if predicted_mood != "unknown":
    mood_folder = os.path.join("music", predicted_mood)
    tracks = os.listdir(mood_folder)
    recommended_track = random.choice(tracks)
    
    # Play the recommended track using the pygame mixer
    mixer.init()
    mixer.music.load(os.path.join(mood_folder, recommended_track))
    mixer.music.play()
else:
    print("Could not determine mood or no recommendations available.")
