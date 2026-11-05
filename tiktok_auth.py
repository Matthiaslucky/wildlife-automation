import urllib.parse, hashlib, base64, secrets

client_key = "sbaworw9337wdd0cl5"
redirect_uri = "https://matthiaslucky.pythonanywhere.com/callback" # must match portal EXACTLY
code_verifier = secrets.token_urlsafe(64)
code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode()).digest()
).decode().rstrip("=")

params = {
    "client_key": client_key,
    "scope": "user.info.basic,user.info.stats,video.list",
    "response_type": "code",
    "redirect_uri": redirect_uri,
    "state": secrets.token_urlsafe(16),
    "code_challenge": code_challenge,
    "code_challenge_method": "S256",
}

auth_url = "https://www.tiktok.com/v2/auth/authorize/?" + urllib.parse.urlencode(params)
print(auth_url)
print("verifier:", code_verifier) # save this for token exchange