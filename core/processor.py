from pathlib import Path

from core.caption import build_caption
from services.color import get_color_tags
from services.image import extract_wallpaper_info


def process_folder(folder: Path):
    wallpaper = next(folder.glob("LockScreenZone-WP-*.*"), None)
    preview = folder / "preview.png"

    if not wallpaper or not preview.exists():
        return None

    result = extract_wallpaper_info(wallpaper)
    if not result:
        return None

    wallpaper_id, width, height = result

    category = folder.parent.name
    color_tags = get_color_tags(wallpaper)

    hashtags = " ".join(f"#{t}" for t in [category.capitalize(), *color_tags])

    caption = build_caption(wallpaper_id, width, height, hashtags)

    return {
        "wallpaper": wallpaper,
        "preview": preview,
        "caption": caption,
    }
