import requests
import os
import yt_dlp

SUBREDDIT = "funny"
DOWNLOAD_DIR = "shared/raw"

def get_reddit_videos(limit=3):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    headers = {"User-agent": "Mozilla/5.0"}
    url = f"https://www.reddit.com/r/{SUBREDDIT}/hot.json?limit=20"

    response = requests.get(url, headers=headers)
    data = response.json()

    count = 0
    for post in data["data"]["children"]:
        url = post["data"].get("url_overridden_by_dest", "")
        if "youtube.com" in url or "youtu.be" in url or "v.redd.it" in url:
            try:
                download_video(url)
                count += 1
                if count >= limit:
                    break
            except Exception as e:
                print(f"Error downloading {url}: {e}")

def download_video(url):
    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_DIR}/%(title).80s.%(ext)s',
        'format': 'mp4',
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])