import os
import subprocess

INPUT_DIR = "shared/shorts"
OUTPUT_PATH = "shared/longform/compilation.mp4"

def compile_longform():
    os.makedirs("shared/longform", exist_ok=True)

    temp_list = "shared/shorts_list.txt"
    with open(temp_list, "w") as f:
        for file in os.listdir(INPUT_DIR):
            if file.endswith(".mp4"):
                f.write(f"file '{os.path.join(INPUT_DIR, file)}'\n")

    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", temp_list,
        "-c", "copy", OUTPUT_PATH
    ]
    subprocess.run(cmd, check=True)