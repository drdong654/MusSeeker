from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards import main_keyboard

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет, друг! 👋\n"
        "Добро пожаловать в лучший поиск треков!\n"
        "Просто пришли мне ссылку и я найду mp3 версию :)",
        reply_markup=main_keyboard,
    )
    await message.answer(
        "Ты можешь импортировать видео в формате mp3 и mp4.\n"
        "Что послушаем? 🎵"
    )


@router.message(Command("menu"))
async def menu(message: Message):
    await message.answer("Меню:", reply_markup=main_keyboard)


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Просто пришли мне ссылку и я найду mp3 версию :)")


@router.message(Command("lol"))
async def funny(message: Message):
    await message.answer_sticker(
        "CAACAgIAAxkBAAMiagzWorubEVKzLRUTZ2jD00kI3C8AAkdZAAId0SBLTDROIH-Fiyg7BA"
    )
