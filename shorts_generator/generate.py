import os
import subprocess

INPUT_DIR = "shared/raw"
OUTPUT_DIR = "shared/shorts"
CLIP_LENGTH = 45

def generate_shorts():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".mp4"):
            continue
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, f"short_{filename}")
        cmd = [
            "ffmpeg", "-y", "-i", input_path,
            "-ss", "00:00:05",
            "-t", str(CLIP_LENGTH),
            "-vf", "scale=720:1280",
            "-c:a", "aac", "-b:a", "128k",
            output_path
        ]
        subprocess.run(cmd, check=True)