import os
from dotenv import load_dotenv
from fetcher import fetch_wildlife_footage, generate_voiceover
from generator import render_wildlife_video
from uploader import send_to_tiktok_inbox

load_dotenv()

def run_wildlife_pipeline():
    print("Step 1: Generating Narration Script...")
    script = (
        "In the deep wilderness, survival is a relentless battle of instinct and strategy. "
        "Watch how this predator tracks its target through the dense brush..."
    )
    audio_path = generate_voiceover(script)

    print("Step 2: Fetching 3-4 minute vertical nature clips...")
    clips = fetch_wildlife_footage(query="wildlife predator fight", min_duration=180)

    print("Step 3: Rendering 1080x1920 video with FFmpeg...")
    final_video = render_wildlife_video(clips, audio_path)

    if final_video:
        print("Step 4: Pushing video draft to TikTok Inbox...")
        send_to_tiktok_inbox(final_video, "Wild Animals Battle for Survival #wildlife #documentary")

if __name__ == "__main__":
    run_wildlife_pipeline()
