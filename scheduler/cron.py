import time
import subprocess

INTERVAL_HOURS = 24

def run_bot_cycle():
    subprocess.call(["python3", "reddit_scraper/scrape.py"])
    subprocess.call(["python3", "shorts_generator/generate.py"])
    subprocess.call(["python3", "captionizer/generate_captions.py"])
    subprocess.call(["python3", "thumbnail_generator/create_thumbnail.py"])
    subprocess.call(["python3", "longform_generator/compile.py"])
    subprocess.call(["python3", "uploader_youtube/uploader.py"])

if __name__ == "__main__":
    while True:
        run_bot_cycle()
        print(f"Sleeping for {INTERVAL_HOURS} hours...")
        time.sleep(INTERVAL_HOURS * 3600)