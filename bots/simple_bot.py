import telebot
from telebot.types import Message

bot_client = telebot.TeleBot(token="5365448130:AAHGkZtiEhLODubKjBdm-5KOmHE7nWKkvZM")


@bot_client.message_handler(commands=["start"])
def echo(message: Message):
    bot_client.reply_to(message=message, text=str(message.chat.id))


bot_client.polling()
