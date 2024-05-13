import os
from datetime import datetime

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv

from database import FILE


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!\n"
        "Welcome to your personal Exchange Hrivnya assistant! 🤖💱\n\n"
        "Get USD to UAH exchange rate statistics "
        "using the /get_exchange_rate command."
    )


@dp.message(Command(commands=["get_exchange_rate"]))
async def get_exchange_rate_command_handler(message: Message) -> None:
    file = FSInputFile(FILE.format(date = datetime.now().date()))
    await message.answer("Here you go!")
    await bot.send_document(message.chat.id, file)


async def main() -> None:
    await dp.start_polling(bot)
