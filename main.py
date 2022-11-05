import os
import telebot

API_KEY = os.getenv('API_KEY',"")
bot = telebot.Telebot(API_KEY)

@bot.message_handler(command=['start'])
deg start(message):
  bot.reply_to(message, "")
  
  bot.polling()
