from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

MAX_FILE_SIZE = 50 * 1024 * 1024

DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)