import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    msg = "TOKEN not set in .env"
    raise ValueError(msg)

DOWNLOAD_DIR = "downloads"
MAX_FILE_SIZE = 50 * 1024 * 1024
