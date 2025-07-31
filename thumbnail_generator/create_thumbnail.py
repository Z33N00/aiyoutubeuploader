from PIL import Image, ImageDraw, ImageFont
import os

INPUT_DIR = "shared/shorts"
THUMBNAIL_DIR = "shared/thumbnails"

def create_thumbnails():
    os.makedirs(THUMBNAIL_DIR, exist_ok=True)
    for file in os.listdir(INPUT_DIR):
        if not file.endswith(".mp4"):
            continue

        base_name = file.replace(".mp4", "")
        output_path = os.path.join(THUMBNAIL_DIR, f"{base_name}.jpg")

        img = Image.new("RGB", (1280, 720), color=(20, 20, 20))
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 64)
        except:
            font = ImageFont.load_default()

        text = f"🔥 Funny Fail #{base_name[-3:]} 😂"
        draw.text((50, 300), text, fill="white", font=font)
        img.save(output_path)