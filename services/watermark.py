import os
import requests
from PIL import Image, ImageDraw, ImageFont

FONT_URL = "https://github.com/google/fonts/raw/main/apache/roboto/Roboto-Bold.ttf"
FONT_PATH = "Roboto-Bold.ttf"

def get_font(size):
    
    if not os.path.exists(FONT_PATH):
        r = requests.get(FONT_URL)
        with open(FONT_PATH, "wb") as f:
            f.write(r.content)

    return ImageFont.truetype(FONT_PATH, size)


def add_watermark(image_path, text="@LockScreenZone"):
    image = Image.open(image_path).convert("RGBA")

    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
  ‌
    font_size = int(image.width * 0.25) 

    font = get_font(font_size)

    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (image.width - text_w) // 2
    y = (image.height - text_h) // 2

    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

    return Image.alpha_composite(image, overlay).convert("RGB")