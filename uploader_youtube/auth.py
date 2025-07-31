import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CREDENTIALS_FILE = "uploader_youtube/client_secret.json"
TOKEN_FILE = "token.pickle"

def get_authenticated_service():
    print("🔐 Starting YouTube authentication flow...")
    credentials = None

    # Load existing token if present
    if os.path.exists(TOKEN_FILE):
        print("🔑 Loading existing token...")
        with open(TOKEN_FILE, "rb") as token:
            credentials = pickle.load(token)

    # Check if credentials are missing or invalid
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print("♻️ Refreshing expired credentials...")
            credentials.refresh(Request())
        else:
            print("🌐 No valid credentials, starting new flow...")
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            # Start flow using local web server
            credentials = flow.run_local_server(port=8080)

        # Save token for future use
        print("💾 Saving new token...")
        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(credentials, token)

    print("✅ Auth flow complete. Returning YouTube service...")
    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

# Trigger auth flow when script is run directly
if __name__ == "__main__":
    get_authenticated_service()

