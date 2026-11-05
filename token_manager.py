import os
import json
import requests

CLIENT_KEY = os.getenv("TIKTOK_CLIENT_KEY", "sbaworw9337wdd0cl5")
CLIENT_SECRET = os.getenv("TIKTOK_CLIENT_SECRET", "10Y0bzW5YJg39yTI1PZcm8vYnUYoodeEP")
TOKEN_URL = "https://open.tiktokapis.com/v2/oauth/token/"
TOKEN_FILE = "tokens.json"

def save_tokens(token_data):
    """Saves updated tokens to local JSON storage."""
    with open(TOKEN_FILE, "w") as f:
        json.dump(token_data, f, indent=4)
    print("Tokens saved successfully.")

def load_tokens():
    """Loads existing tokens from local JSON storage."""
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return json.load(f)
    return None

def refresh_access_token():
    """Requests a new access token using the stored refresh_token."""
    tokens = load_tokens()
    if not tokens or "refresh_token" not in tokens:
        print("Error: No refresh token found. Run initial auth first.")
        return None

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }

    payload = {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": tokens["refresh_token"]
    }

    response = requests.post(TOKEN_URL, headers=headers, data=payload)
    res_data = response.json()

    if "access_token" in res_data:
        new_tokens = {
            "access_token": res_data["access_token"],
            "refresh_token": res_data.get("refresh_token", tokens["refresh_token"]),
            "expires_in": res_data.get("expires_in", 86400),
            "open_id": res_data.get("open_id", tokens.get("open_id", ""))
        }
        save_tokens(new_tokens)
        return new_tokens["access_token"]
    else:
        print("Refresh failed:", res_data)
        return None

def get_valid_access_token():
    """Returns the current access_token, or refreshes if missing."""
    tokens = load_tokens()
    if not tokens:
        return refresh_access_token()
    return tokens.get("access_token")

if __name__ == "__main__":
    print("Testing token loader...")
    print("Current Access Token:", get_valid_access_token())
