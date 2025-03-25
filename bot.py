import asyncio
from aiogram import Bot, Dispatcher, types

# Bot token aur admin chat ID
TOKEN = "7631472471:AAEBhuruWc4175Vm8Hyx8R7vUTjx3yO7lJk"
ADMIN_ID = 5539061712  

# Bot initialize karna
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Start command ka response
@dp.message(commands=['start'])
async def send_welcome(message: types.Message):
    if message.chat.id == ADMIN_ID:
        await message.answer("🔥 *स्वागत है, Admin!* 🔥", parse_mode="Markdown")
    else:
        await message.answer("👋 *स्वागत है!* यह एक टेस्ट बॉट है।", parse_mode="Markdown")

# Main function to run bot
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Run bot
if __name__ == "__main__":
    asyncio.run(main())
