#Made by SahilXCodes 
#Telegram - @Its_Sahil_Ansari

from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot
from config import HELP_TXT, START_MSG, CMD_TXT
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

#-------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Back', callback_data='start'),
                        InlineKeyboardButton("Close", callback_data='close')
                    ]
                ]
            )
        )
elif data == "commands":
        await query.message.edit_text(
            text=CMD_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Close", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Help", callback_data='help'),
                InlineKeyboardButton("Close", callback_data='close')]
            ])
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass      
