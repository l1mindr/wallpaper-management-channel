from pathlib import Path
from PIL import Image
import re

images_dir = Path("images")

for folder in sorted(images_dir.iterdir(), key=lambda x: int(x.name)):
    if not folder.is_dir():
        continue

    wallpaper = next(folder.glob("LockScreenZone-WP-*.*"), None)

    if wallpaper is None:
        print(f"❌ Wallpaper not found in {folder.name}")
        continue

    match = re.search(r"WP-(\d+)", wallpaper.stem)

    if not match:
        print(f"❌ Invalid filename: {wallpaper.name}")
        continue

    wallpaper_id = int(match.group(1))

    with Image.open(wallpaper) as img:
        width, height = img.size

    print("=" * 60)
    print(f"""📱 والپیپر {wallpaper_id}
    رزولوشن: ‎[{width}]×[{height}]
    مناسب برای آیفون 🍎
    دانلود فایل 👇

    #LockScreenZone #WP{wallpaper_id:03d} #Vespa #Green
    @LockScreenZone
    """)
