from PIL import Image, ImageDraw, ImageFont


def add_watermark(image_path, text="@LockScreenZone"):
    image = Image.open(image_path).convert("RGBA")

    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # 🔥 فونت بزرگ
    font_size = max(200, image.width // 5)

    try:
        font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    except OSError:
        font = ImageFont.load_default()

    # 📍 محاسبه مرکز متن
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (image.width - text_w) // 2
    y = (image.height - text_h) // 2

    # ⚪ متن سفید ساده
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

    result = Image.alpha_composite(image, overlay)

    return result.convert("RGB")
