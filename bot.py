import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# अपना बॉट टोकन डालें
TOKEN = "7631472471:AAEBhuruWc4175Vm8Hyx8R7vUTjx3yO7lJk"
ADMIN_ID = 5539061712  # अपना Telegram Chat ID डालें

# बॉट और डिस्पैचर सेट करें
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(commands=['start'])
async def start_command(message: Message):
    if message.chat.id == ADMIN_ID:
        welcome_text = "<b><i>🚀 स्वागत है, महाराज! आपका बॉट एक्टिव हो गया। 🎉</i></b>"
        await message.reply(welcome_text)  # ✅ Indentation सही किया गया

async def main():
    print("✅ बॉट स्टार्ट हो गया...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
