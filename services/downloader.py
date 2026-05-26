import os
import re
import uuid

import yt_dlp

from config import DOWNLOAD_DIR


def is_supported_url(text: str) -> bool:
    return bool(re.match(r"https?://", text))


def download_music(url: str) -> str | None:
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    file_id = uuid.uuid4().hex
    opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(DOWNLOAD_DIR, file_id + ".%(ext)s"),
        "quiet": True,
        "keepvideo": False,
        "extractor_args": {"youtube": {"player_client": ["mweb", "android"]}},
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}],
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
    except Exception:
        return None

    mp3 = os.path.join(DOWNLOAD_DIR, file_id + ".mp3")
    if os.path.exists(mp3):
        return mp3
    return None
