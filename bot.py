from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Bot token aur admin chat ID
TOKEN = "7631472471:AAEBhuruWc4175Vm8Hyx8R7vUTjx3yO7lJk"
ADMIN_ID = 5539061712  

# Bot aur dispatcher initialize karna
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Start command ka response
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if message.chat.id == ADMIN_ID:
        await message.answer("🔥 *स्वागत है, Admin!* 🔥", parse_mode="Markdown")
    else:
        await message.answer("👋 *स्वागत है!* यह एक टेस्ट बॉट है।", parse_mode="Markdown")

# Bot ko start karna
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
