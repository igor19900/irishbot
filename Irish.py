import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

TOKEN = "7896777201:AAGRAPZW2Er_TGZlRUYlmc5AmLj5xCkmsEU"
CHAT_ID = 1234933498

bot = Bot(token=TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()

# Список комплиментов
compliments = [
    "Ты — настоящее сокровище в моей жизни. С каждым днём я это чувствую всё сильнее.",
    "С тобой я самый счастливый человек на свете.",
    "Ты мой нежнейший котёнок. Просто не могу налюбоваться тобой.",
    "Каждое утро, просыпаясь рядом, я понимаю, как мне повезло с тобой.",
    "Твоя улыбка — мой личный антистресс.",
    "Я хочу прожить с тобой всю жизнь — и каждую минуту наполнять любовью.",
    "Когда ты рядом, всё вокруг становится светлее и теплее.",
    "Ты — самое прекрасное, что произошло в моей жизни.",
    "Я влюбляюсь в тебя снова и снова, даже просто глядя на тебя.",
    "Даже когда ты злишься — ты очаровательна. И это правда.",
    "Ты самая-самая лучшая на свете.",
    "Ты — женщина моей мечты. И каждый день с тобой — доказательство, что мечты сбываются.",
    "Ты — мой лучик солнца, даже в пасмурные дни.",
    "С тобой каждый день — это приключение, которое хочется переживать снова и снова.",
    "Я благодарен судьбе за тебя — просто за то, что ты есть.",
    "Когда ты смотришь на меня — у меня внутри всё замирает.",
    "Ты делаешь мою жизнь осмысленной, красивой и по-настоящему живой.",
    "Ты моя Ирандель.",
    "В тебе столько тепла, что мне хватает его даже в самые сложные дни.",
    "Хочу прожить с тобой всю жизнь."
]

@dp.message(Command("start"))
async def start(message: Message):
    kb = ReplyKeyboardBuilder()
    kb.button(text="❤️ Любимой Иришке")
    await message.answer(
        "Привет! Я бот-комплимент от твоего мужа 🥰\nНажми кнопку, и я скажу тебе что-то тёплое.",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )

    global CHAT_ID
    CHAT_ID = message.chat.id  # Сохраняем ID, если запускается вручную

@dp.message(lambda msg: msg.text == "❤️ Любимой Иришке")
async def send_compliment(message: Message):
    compliment = random.choice(compliments)
    await message.answer(compliment)

async def scheduled_compliment():
    if CHAT_ID:
        compliment = random.choice(compliments)
        await bot.send_message(chat_id=CHAT_ID, text=compliment)

async def main():
    # Рассылка в 08:00
    scheduler.add_job(scheduled_compliment, CronTrigger(hour=8, minute=0))
    # Рассылка в 21:00
    scheduler.add_job(scheduled_compliment, CronTrigger(hour=21, minute=0))
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())