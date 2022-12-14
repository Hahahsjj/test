import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import os
from text import START_TXT, RIP_TXT, MYPLAN_TXT, PLANS_TXT, ABOUT_TXT, AVAILABLEOTT_TXT


# bot
bot_token = os.environ.get("TOKEN", "")
api_hash = os.environ.get("HASH", "") 
api_id = os.environ.get("ID", "")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)

@app.on_message(filters.command(["start"]))
def send_help(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, START_TXT, reply_to_message_id=message.id, disable_web_page_preview=True)
reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton("❤About", "https://t.me/Legend_Shivam_7")]])), reply_to_message_id=message.id)



@app.on_message(filters.command(["rip"]))
def send_help(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, RIP_TXT, reply_to_message_id=message.id, disable_web_page_preview=True)

@app.on_message(filters.command(["plans"]))
def send_help(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, PLANS_TXT, reply_to_message_id=message.id, disable_web_page_preview=True)

@app.on_message(filters.command(["about"]))
def send_help(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, ABOUT_TXT, reply_to_message_id=message.id, disable_web_page_preview=True)

@app.on_message(filters.command(["availableotts"]))
def send_help(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, AVAILABLEOTT_TXT, reply_to_message_id=message.id, disable_web_page_preview=True)

@app.on_message(filters.command(["myplan"]))
def send_help(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, MYPLAN_TXT, reply_to_message_id=message.id, disable_web_page_preview=True)



print("Bot Starting")
app.run()
