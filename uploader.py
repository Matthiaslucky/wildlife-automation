import os
import requests
from token_manager import get_valid_access_token

INIT_UPLOAD_URL = "https://open.tiktokapis.com/v2/post/publish/video/init/"

def initialize_video_upload(video_size_bytes):
    """Initializes a chunked or single video upload session with TikTok."""
    access_token = get_valid_access_token()
    if not access_token:
        print("Error: Unable to acquire valid access token.")
        return None

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=UTF-8"
    }

    # Standard Direct Upload payload structure
    payload = {
        "source_info": {
            "source": "FILE_UPLOAD",
            "video_size": video_size_bytes,
            "chunk_size": video_size_bytes,
            "total_chunk_count": 1
        }
    }

    response = requests.post(INIT_UPLOAD_URL, headers=headers, json=payload)
    res_data = response.json()

    if res_data.get("error", {}).get("code") == "ok":
        upload_url = res_data["data"]["upload_url"]
        publish_id = res_data["data"]["publish_id"]
        print("Upload Session Initialized Successfully!")
        print(f"Publish ID: {publish_id}")
        return upload_url, publish_id
    else:
        print("Failed to initialize upload:", res_data)
        return None, None

if __name__ == "__main__":
    print("TikTok Uploader Module Ready.")
