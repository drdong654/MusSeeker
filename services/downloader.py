import os
import re
import uuid
import logging
from urllib.parse import urlparse

import yt_dlp

from config import DOWNLOAD_DIR


logger = logging.getLogger(__name__)


def is_supported_url(text: str) -> bool:
    if not re.match(r"https?://", text):
        return False

    parsed = urlparse(text)
    host = (parsed.hostname or "").lower()

    allowed_hosts = {
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
        "music.youtube.com",
        "youtu.be",
        "www.youtu.be",
    }

    if host not in allowed_hosts:
        return False

    return bool(parsed.path)


def download_music(url: str) -> str | None:
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    po_token = os.getenv("YTDLP_PO_TOKEN", "").strip()
    client_variants = [
        ["mweb", "android"],
        ["android", "web"],
        ["web", "mweb"],
    ]

    for player_client in client_variants:
        file_id = uuid.uuid4().hex
        extractor_args = {"youtube": {"player_client": player_client}}
        if po_token:
            extractor_args["youtube"]["po_token"] = [po_token]

        opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(DOWNLOAD_DIR, file_id + ".%(ext)s"),
            "quiet": True,
            "no_warnings": True,
            "keepvideo": False,
            "extractor_args": extractor_args,
            "postprocessors": [
                {"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}
            ],
        }

        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
        except Exception as exc:
            logger.warning(
                "yt-dlp failed for clients=%s with %s: %s",
                ",".join(player_client),
                type(exc).__name__,
                exc,
            )
            continue

        mp3 = os.path.join(DOWNLOAD_DIR, file_id + ".mp3")
        if os.path.exists(mp3):
            return mp3

    return None
