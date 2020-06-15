import telebot
TOKEN = '1226621202:AAGVkMsvYOPElRa4pU7hDEJV_BgtA4Ep4IY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
	bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)
