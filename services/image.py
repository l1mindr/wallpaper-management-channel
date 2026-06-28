import re
from PIL import Image


def extract_wallpaper_info(path):
    match = re.search(r"WP-(\d+)", path.stem)
    if not match:
        return None

    wallpaper_id = int(match.group(1))

    with Image.open(path) as img:
        width, height = img.size

    return wallpaper_id, width, height
