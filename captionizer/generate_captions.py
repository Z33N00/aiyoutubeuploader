import whisper
import os

INPUT_DIR = "shared/shorts"
CAPTION_DIR = "shared/captions"

def generate_captions():
    os.makedirs(CAPTION_DIR, exist_ok=True)
    model = whisper.load_model("base")

    for file in os.listdir(INPUT_DIR):
        if not file.endswith(".mp4"):
            continue
        input_path = os.path.join(INPUT_DIR, file)
        output_path = os.path.join(CAPTION_DIR, file.replace(".mp4", ".srt"))

        print(f"Transcribing {file}...")
        result = model.transcribe(input_path)
        with open(output_path, "w", encoding="utf-8") as f:
            for i, segment in enumerate(result["segments"]):
                f.write(f"{i+1}\n")
                start = segment['start']
                end = segment['end']
                f.write(f"{format_time(start)} --> {format_time(end)}\n")
                f.write(segment['text'].strip() + "\n\n")

def format_time(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int((t - int(t)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"