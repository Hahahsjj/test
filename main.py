import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import os
from texts import 


# bot
bot_token = os.environ.get("TOKEN", "")
api_hash = os.environ.get("HASH", "") 
api_id = os.environ.get("ID", "")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)


print("Bot Starting")
app.run()
