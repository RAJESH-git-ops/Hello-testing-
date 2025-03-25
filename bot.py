import requests
import time

# अपना Telegram Bot Token और Chat ID डालें
TOKEN = "7631472471:AAEBhuruWc4175Vm8Hyx8R7vUTjx3yO7lJk"
ADMIN_ID = "5539061712"

# Telegram API URL
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Welcome Message
WELCOME_MESSAGE = "🚀 स्वागत है, महाराज! आपका बॉट एक्टिव हो गया। 🎉"

def send_message(chat_id, text):
    """बॉट से मैसेज भेजने का फ़ंक्शन"""
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    requests.post(URL, data=payload)

# ✅ बॉट स्टार्ट होते ही Admin को मैसेज भेजेगा
send_message(ADMIN_ID, WELCOME_MESSAGE)

print("✅ बॉट GitHub Codespaces में स्टार्ट हो गया...")

# बॉट को हमेशा चालू रखने के लिए Loop
while True:
    time.sleep(10)  # हर 10 सेकंड में बॉट एक्टिव रहेगा
