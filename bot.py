import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

# Загружаем .env только локально.
# На Railway BOT_TOKEN придёт из вкладки Variables.
load_dotenv(Path(__file__).parent / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
REDIRECT_LINK = "https://t.me/+pMvq4cwK0JJkZDk0"

if not BOT_TOKEN:
    raise ValueError(
        "BOT_TOKEN не найден. Локально проверь .env, "
        "на Railway добавь BOT_TOKEN во вкладке Variables."
    )

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👉 Перейти",
                    url=REDIRECT_LINK
                )
            ]
        ]
    )

    await message.answer(
        text="Привет! Нажми на кнопку ниже, чтобы перейти:",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())