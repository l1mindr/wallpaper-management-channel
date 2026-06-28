from utils.text import to_persian_digits


def build_caption(wallpaper_id: int, width: int, height: int, hashtags: str):
    apple = "🍎" if wallpaper_id % 2 else "🍏"

    return "\n".join(
        [
            f"📱 والپیپر {to_persian_digits(str(wallpaper_id))}",
            f"رزولوشن: [{height}]×[{width}]",
            f"مناسب برای آیفون {apple}",
            "دانلود فایل 👇",
            "",
            f"#LockScreenZone #WP{wallpaper_id:03d} {hashtags}",
            "@LockScreenZone",
        ]
    )
