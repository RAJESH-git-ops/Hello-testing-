from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# यहाँ अपना बॉट टोकन डालें
TOKEN = "7631472471:AAEBhuruWc4175Vm8Hyx8R7vUTjx3yO7lJk"
ADMIN_ID = 5539061712  # अपना Telegram Chat ID डालें

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    if message.chat.id == ADMIN_ID:
        welcome_text = "<b><i>🚀 स्वागत है, महाराज! आपका बॉट एक्टिव हो गया। 🎉</i></b>"
        await message.reply(welcome_text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)