from pathlib import Path

from core.processor import process_folder
from telegram.service import send_to_telegram
from utils.logger import setup_logger

logger = setup_logger()

images_dir = Path("images")


def safe_int(name: str) -> int:
    try:
        return int(name)
    except ValueError:
        return float("inf")


logger.info("🚀 Starting wallpaper upload process...")

for category in sorted(images_dir.iterdir()):
    if not category.is_dir():
        continue

    logger.info(f"📁 Category: {category.name}")

    for folder in sorted(category.iterdir(), key=lambda x: safe_int(x.name)):
        if not folder.is_dir():
            continue

        logger.info(f"➡️ Processing folder: {folder.name}")

        data = process_folder(folder)

        if not data:
            logger.warning(f"⚠️ Skipped folder: {folder.name}")
            continue

        try:
            send_to_telegram(data)
            logger.info(f"✅ Sent: {folder.name}")
        except Exception as e:
            logger.error(f"❌ Failed folder {folder.name}: {e}")

logger.info("🎉 Finished all uploads")
