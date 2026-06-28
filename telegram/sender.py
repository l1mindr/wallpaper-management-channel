import logging
import tempfile
from pathlib import Path

import requests

from config.config import BOT_TOKEN, CHANNEL_ID
from services.watermark import add_watermark

logger = logging.getLogger("wallpaper_bot")


def send_preview(preview_path: Path, caption: str) -> int:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    logger.info(f"📤 Sending preview → {preview_path}")

    try:
        # اضافه کردن واترمارک
        watermarked = add_watermark(preview_path)

        # ذخیره موقت برای ارسال
        with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp:
            watermarked.save(tmp.name, quality=95)

            with open(tmp.name, "rb") as photo:
                res = requests.post(
                    url,
                    data={
                        "chat_id": CHANNEL_ID,
                        "caption": caption,
                    },
                    files={"photo": photo},
                    timeout=30,
                )

        result = res.json()

        if not result.get("ok"):
            logger.error(f"❌ Preview failed → {result}")
            raise Exception(result)

        message_id = result["result"]["message_id"]

        logger.info(f"✅ Preview sent | message_id={message_id}")
        return message_id

    except Exception as e:
        logger.error(f"💥 Exception in send_preview → {e}")
        raise


def send_wallpaper(file_path: Path, reply_to: int):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

    logger.info(f"📦 Sending wallpaper → {file_path} | reply_to={reply_to}")

    try:
        with open(file_path, "rb") as f:
            res = requests.post(
                url,
                data={
                    "chat_id": CHANNEL_ID,
                    "reply_to_message_id": reply_to,
                },
                files={"document": f},
                timeout=30,
            )

        result = res.json()

        if not result.get("ok"):
            logger.error(f"❌ Wallpaper failed → {result}")
            raise Exception(result)

        logger.info("✅ Wallpaper sent successfully")

    except Exception as e:
        logger.error(f"💥 Exception in send_wallpaper → {e}")
        raise
