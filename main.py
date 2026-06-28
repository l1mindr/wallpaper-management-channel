import re
from pathlib import Path

from PIL import Image

from color_detector import get_color_tags
from pinter import printer

images_dir = Path("images")

# همه پوشه‌های دسته‌بندی (Minimal, Nature, ...)
for category in sorted(images_dir.iterdir()):
    if not category.is_dir():
        continue

    # همه پوشه‌های شماره (1, 2, 3, ...)
    for folder in sorted(category.iterdir(), key=lambda x: int(x.name)):
        if not folder.is_dir():
            continue

        wallpaper = next(folder.glob("LockScreenZone-WP-*.*"), None)

        if wallpaper is None:
            print(f"❌ Wallpaper not found in {folder}")
            continue

        match = re.search(r"WP-(\d+)", wallpaper.stem)

        if not match:
            print(f"❌ Invalid filename: {wallpaper.name}")
            continue

        wallpaper_id = int(match.group(1))

        with Image.open(wallpaper) as img:
            width, height = img.size

        color_tags = get_color_tags(wallpaper)

        tags = [category.name.capitalize()]
        tags.extend(color_tags)

        hashtags = " ".join(f"#{tag}" for tag in tags)

        print("=" * 60)
        printer(wallpaper_id, width, height, hashtags)
