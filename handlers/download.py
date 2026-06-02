import asyncio
import os

from aiogram import Router
from aiogram.types import CallbackQuery, FSInputFile, Message

from config import MAX_FILE_SIZE
from keyboards import after_download_keyboard, main_keyboard
from services.downloader import download_music, is_supported_url
from config import DOWNLOAD_DIR

router = Router()


@router.message()
async def mus_download(message: Message):
    text = message.text or ""
    url = text.strip()

    if url == "🎵 Скачать трек":
        await message.answer("Отправь мне ссылку на видео:")
        return

    if url in ("❓ Помощь", "/help"):
        await message.answer("Просто пришли мне ссылку и я найду mp3 версию :)")
        return

    if url in ("😂 Прикол", "/lol"):
        await message.answer_sticker(
            "CAACAgIAAxkBAAMiagzWorubEVKzLRUTZ2jD00kI3C8AAkdZAAId0SBLTDROIH-Fiyg7BA"
        )
        return

    if not is_supported_url(url):
        await message.answer(
            "Нужна ссылка именно на YouTube (youtube.com или youtu.be)."
        )
        return

    await message.answer("Начинаю скачивание...")

    file_path = await asyncio.to_thread(download_music, url)

    if file_path is None:
        await message.answer(
            "Не удалось скачать трек. Проверь ссылку и попробуй снова."
        )
        return

    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE:
        os.remove(file_path)
        await message.answer(
            "Файл слишком большой — Telegram не поддерживает файлы больше 50 MB."
        )
        return

    audio = FSInputFile(file_path)
    try:
        await message.answer_audio(audio, reply_markup=after_download_keyboard())
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


@router.callback_query()
async def handle_callback(callback: CallbackQuery):
    await callback.answer()
    if callback.data == "menu":
        await callback.message.answer("Меню:", reply_markup=main_keyboard)
