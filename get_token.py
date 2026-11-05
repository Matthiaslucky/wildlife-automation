import requests
from urllib.parse import unquote

# 1. Endpoint Configuration
url = "https://open.tiktokapis.com/v2/oauth/token/"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cache-Control": "no-cache"
}

# 2. Paste the RAW code string directly from your browser's address bar:
raw_code = "5WcGc223gU7tjfu4oPWouloC3VUeVc3s6mgoh5ik8Q_JH5CUOBdJZBB2ZqJjWjghRT3CQ3gJB3d-CfdIXkryqrsi9kWByltaJjLrKNQOalg7GwW54C9e5I_eVYp_B9WQ6DsqTh9ROEUi1ZFDuoX3RCN9Iou99v6PzaBermhyU-77XtGLnB8sTNpt_3mDA5qiL38iVqZBweMYbnL6TbtA4hEo7iD35nTq9oyfbvdjpo_K91cppQ_3IwOSj7Y%2Av%215683.s1"
code = unquote(raw_code).strip()

# 3. Payload with exact matching verifier
payload = {
    "client_key": "sbaworw9337wdd0cl5",
    "client_secret": "10Y8bzW5YJg39yTIiPZcm0vYnUYodeEP",
    "code": code,
    "grant_type": "authorization_code",
    "redirect_uri": "https://matthiaslucky.pythonanywhere.com/callback",
    "code_verifier": " GD-yuA57XduRA82VOA9b1SqSC6ZpxTNv9WmTiSnUdpj4D9RkCF6COFm_dBLP6eduBhKz9wSx1333PYvvQAYJkw"
}

# 4. Request Access Token
response = requests.post(url, headers=headers, data=payload)
print("\n--- TOKEN RESPONSE ---")
print(response.json())
