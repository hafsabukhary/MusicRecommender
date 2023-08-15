# Mood-Based Music Recommender using TextBlob

This code snippet demonstrates a basic mood-based music recommender using the TextBlob library for sentiment analysis and the pygame library for audio playback. The user inputs their mood (text or voice), and the code recommends a track from a local music library based on the detected mood.

## Prerequisites

- Python installed on your system
- Install the required libraries using `pip`:
  ```
  pip install textblob pygame
  ```

## Code Explanation

```python
from textblob import TextBlob
from pygame import mixer
import os
import random

# Get user input (text or voice)
user_input = input("Enter your mood: ")

# Perform sentiment analysis on user input using TextBlob
sentiment = TextBlob(user_input).sentiment
predicted_mood = "happy" if sentiment.polarity > 0 else "sad"  # Simplified logic

# Recommend tracks from the local music library based on predicted mood
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
```

## Usage

1. Run the main.py in a Python environment.
2. Enter your mood (e.g., "happy," "sad") as text input.
3. The code will perform sentiment analysis and play a recommended music track from the local music library based on the detected mood.

## Notes

- This code uses TextBlob for sentiment analysis, which provides basic polarity scores.
- The pygame library is used for audio playback.
- Replace the `"music"` folder with the actual path to your local music library.
- For more accurate sentiment analysis, consider using more advanced sentiment analysis models.
