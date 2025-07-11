#Made by SahilXCodes 
#Telegram - @Its_Sahil_Ansari

import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from database.database import present_admin

from bot import Bot
from config import OWNER_ID, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode

#-------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------

@Bot.on_message(filters.private & ~filters.command(['start','users','broadcast','batch','genlink','stats', 'forcesub1', 'forcesub2', 'viewforce', 'nbatch', 'add_admin', 'del_admin', 'admins']))
async def channel_post(client: Client, message: Message):
    user_id = message.from_user.id
    is_admin = await present_admin(user_id)
    
    if user_id != OWNER_ID and not is_admin:
        return
    
    reply_text = await message.reply_text("Please Wait...!", quote=True)
    try:
        post_message = await message.copy(chat_id=client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id=client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📫 ʏᴏᴜʀ ᴜʀʟ", url=f'https://telegram.me/share/url?url={link}')]])

    await reply_text.edit(f"<b>Here is your link</b>\n\n{link}", reply_markup=reply_markup, disable_web_page_preview=True)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

#-------------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------------

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📫 ʏᴏᴜʀ ᴜʀʟ​", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
