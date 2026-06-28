from pathlib import Path

from telegram.sender import send_preview, send_wallpaper


def send_to_telegram(data):
    preview = Path(data["preview"])
    wallpaper = Path(data["wallpaper"])

    msg_id = send_preview(preview, data["caption"])
    send_wallpaper(wallpaper, msg_id)
