# 🤖 AI Shorts & YouTube Uploader

---

🚀 Features

🧠 Auto pulls videos from Reddit + YouTube

✂️ Auto generates Shorts & long-form content

💬 Auto captions with Whisper

🔤 Auto hashtags + emojis

🖼️ Auto thumbnail generation

⏰ Daily upload scheduler

🐳 Fully Dockerized – just plug & play

✅ YouTube OAuth pre-configured with token.pickle



---

🛠️ Requirements

Docker & Docker Compose

YouTube API access (via client_secret.json)

YouTube OAuth token (token.pickle) — created by running auth.py



---

📁 Setup Instructions

1. Clone the repo:

git clone https://github.com/Z33N00/aiyoutubeuploader.git
cd aiyoutubeuploader


2. Make sure these 2 files are in the root:

client_secret.json

token.pickle



3. Run the container:

docker compose up




---

🔐 Need YouTube API Auth?

If you haven't already:

cd uploader_youtube
python3 auth.py

This will launch the YouTube login in your browser and generate token.pickle.
