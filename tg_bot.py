import ptbot

TG_TOKEN = '6298309827:AAFKFkaDBHF2eIzmvwz0M_q80qCDbn6TPXI'  # подставьте свой ключ API
TG_CHAT_ID = '933120886'  # подставьте свой ID
bot = ptbot.Bot(TG_TOKEN)
bot.send_message(TG_CHAT_ID, "Бот запущен")