from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

MAX_FILE_SIZE = 50 * 1024 * 1024

DOWNLOAD_DIR = Path("/app/downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)