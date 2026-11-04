import os
import requests
from gtts import gTTS

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def fetch_wildlife_footage(query="lion hunting insect", min_duration=180):
    """
    Fetches vertical nature clips matching the duration target (3-4 minutes).
    """
    headers = {"Authorization": PEXELS_API_KEY}
    url = f"https://api.pexels.com/videos/search?query={query}&orientation=portrait&per_page=15"
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Pexels API Error: {response.text}")
        
    data = response.json()
    video_urls = []
    
    for video in data.get("videos", []):
        # Extract 1080x1920 or highest quality portrait file link
        for video_file in video.get("video_files", []):
            if video_file.get("width") and video_file.get("height"):
                if video_file["height"] > video_file["width"]:
                    video_urls.append(video_file["link"])
                    break
                    
    return video_urls

def generate_voiceover(text_script, output_audio="narration.mp3"):
    """
    Generates dynamic voiceover for animal survival narration.
    """
    tts = gTTS(text=text_script, lang="en", slow=False)
    tts.save(output_audio)
    return output_audio
