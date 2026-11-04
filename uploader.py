import os
import requests

TIKTOK_ACCESS_TOKEN = os.getenv("TIKTOK_USER_ACCESS_TOKEN")

def send_to_tiktok_inbox(video_file_path, video_title):
    """
    Initiates TikTok Media Upload (Inbox Draft mode).
    Pushes video to your phone inbox to publish safely with 1-tap.
    """
    file_size = os.path.getsize(video_file_path)
    
    # 1. Initialize Inbox Upload
    init_url = "https://open.tiktokapis.com/v2/post/publish/inbox/video/init/"
    headers = {
        "Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}",
        "Content-Type": "application/json; charset=UTF-8"
    }
    payload = {
        "source_info": {
            "source": "FILE_UPLOAD",
            "video_size": file_size,
            "chunk_size": file_size,
            "total_chunk_count": 1
        }
    }
    
    init_res = requests.post(init_url, headers=headers, json=payload)
    if init_res.status_code != 200:
        print(f"Failed to init TikTok Upload: {init_res.text}")
        return False
        
    res_data = init_res.json().get("data", {})
    upload_url = res_data.get("upload_url")
    publish_id = res_data.get("publish_id")

    # 2. Upload Binary File to TikTok Upload URL
    with open(video_file_path, "rb") as video_file:
        upload_headers = {
            "Content-Type": "video/mp4",
            "Content-Length": str(file_size),
            "Content-Range": f"bytes 0-{file_size-1}/{file_size}"
        }
        upload_res = requests.put(upload_url, headers=upload_headers, data=video_file)
        
    if upload_res.status_code in [200, 201]:
        print(f"SUCCESS: Video pushed to TikTok Inbox! Publish ID: {publish_id}")
        return True
    else:
        print(f"Upload failed: {upload_res.text}")
        return False
