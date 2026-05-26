from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
MAX_FILE_SIZE = 50 * 1024 * 1024
