import os
import telebot

API_KEY = os.getenv('API_KEY',"5598963437:AAG9roGF9xQ_9HNiRcpwKdCpGi1k3jCMGKk")
bot = telebot.Telebot(API_KEY)

@bot.message_handler(command=['start'])
deg start(message):
  bot.reply_to(message, "")
  
  bot.polling()
