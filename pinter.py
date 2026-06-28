def to_persian_digits(text: str) -> str:
    return text.translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹"))


def printer(wallpaper_id: str, width: int, height: int, hashtags: str):
    apple = "🍎" if int(wallpaper_id) % 2 else "🍏"

    lines = [
        f"📱 والپیپر {to_persian_digits(str(wallpaper_id))}",
        "",
        f"رزولوشن: [{width}]×[{height}]",
        f"مناسب برای آیفون {apple}",
        "",
        "دانلود فایل 👇",
        "",
        f"#LockScreenZone #WP{wallpaper_id:03d} {hashtags}",
        "@LockScreenZone",
    ]

    print("\n".join(lines))
