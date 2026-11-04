import subprocess
import os

def render_wildlife_video(video_clips_list, narration_audio, output_mp4="final_wildlife.mp4"):
    """
    Stitches nature clips to reach 3-4 mins (180-240s) using FFmpeg on EC2.
    """
    # 1. Create temporary file list for FFmpeg concatenation
    with open("clips.txt", "w") as f:
        for clip_path in video_clips_list:
            f.write(f"file '{clip_path}'\n")

    # 2. FFmpeg command: Concatenate clips + overlay voiceover + format 1080x1920
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0", "-i", "clips.txt",
        "-i", narration_audio,
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        output_mp4
    ]

    result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FFmpeg Error: {result.stderr}")
        return None
        
    return output_mp4
