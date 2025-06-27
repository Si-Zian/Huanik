#Made by SahilXCodes 
#Telegram - @Its_Sahil_Ansari

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram.enums import ChatMemberStatus
from bot import Bot
from config import OWNER_ID
from database.database import present_admin
from helper_func import encode, get_message_id, get_messages

#-------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------

@Bot.on_message(filters.private & filters.command('batch'))
async def batch(client: Client, message: Message):
    user_id = message.from_user.id
    is_admin = await present_admin(user_id)
    
    if user_id != OWNER_ID and not is_admin:
        return
    
    while True:
        try:
            first_message = await client.ask(text="🚀​Fᴏʀᴡᴀʀᴅ ꜰɪʀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ DB ᴄʜᴀɴɴᴇʟ...! (with Quotes)..\n\n​Oʀ ꜱᴇɴᴅ DB ᴄʜᴀɴɴᴇʟ ᴘᴏꜱᴛ ʟɪɴᴋ​",
                                              chat_id=message.from_user.id,
                                              filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                                              timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("🚫 ᴇʀʀᴏʀ\n\n​​​Iᴛ'ꜱ ɴᴏᴛ ꜰʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴅᴜᴅᴇ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ​...!", quote=True)
            continue

    while True:
        try:
            second_message = await client.ask(text="🚀​Fᴏʀᴡᴀʀᴅ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ ʏᴏᴜʀ DB ᴄʜᴀɴɴᴇʟ...! (with Quotes)..\nOʀ ꜱᴇɴᴅ DB ᴄʜᴀɴɴᴇʟ ᴘᴏꜱᴛ ʟɪɴᴋ​​",
                                               chat_id=message.from_user.id,
                                               filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                                               timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("🚫 ᴇʀʀᴏʀ\n\nIᴛ'ꜱ ɴᴏᴛ ꜰʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴅᴜᴅᴇ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ...!", quote=True)
            continue

    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📫 ʏᴏᴜʀ ᴜʀʟ", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)

#-------------------------------------------------------------------------------------------  

@Bot.on_message(filters.private & filters.command("nbatch"))
async def nbatch(client: Client, message: Message):
    user_id = message.from_user.id
    is_admin = await present_admin(user_id)
    
    if user_id != OWNER_ID and not is_admin:
        return
    
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        await message.reply("❌ Invalid format! Use: /nbatch {number}")
        return
    
    batch_size = int(args[1])
    
    while True:
        try:
            first_message = await client.ask(
                text="🚀 Send DB channel first message link (with Quotes)...",
                chat_id=message.from_user.id,
                filters=(filters.text & ~filters.forwarded),
                timeout=60
            )
        except:
            return
    
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("🚫 Invalid! Send correct DB channel message link.", quote=True)
            continue
    
    s_msg_id = f_msg_id + batch_size - 1  # Adding batch_size to first message ID
    
    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("📫 Your Batch URL", url=f'https://telegram.me/share/url?url={link}')]
    ])
    
    await first_message.reply_text(f"<b>Here is your batch link</b>\n\n{link}", quote=True, reply_markup=reply_markup)

#-------------------------------------------------------------------------------------------

@Bot.on_message(filters.private & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    user_id = message.from_user.id
    is_admin = await present_admin(user_id)
    
    if user_id != OWNER_ID and not is_admin:
        return
    
    while True:
        try:
            channel_message = await client.ask(text="🚀Fᴏʀᴡᴀʀᴅ ꜰɪʀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ DB ᴄʜᴀɴɴᴇʟ...! (with Quotes)..\n​Oʀ ꜱᴇɴᴅ DB ᴄʜᴀɴɴᴇʟ ᴘᴏꜱᴛ ʟɪɴᴋ​",
                                                chat_id=message.from_user.id,
                                                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                                                timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("🚫 ᴇʀʀᴏʀ\n\nɪᴛ'ꜱ ɴᴏᴛ ꜰʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴅᴜᴅᴇ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ​...!", quote=True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📫 ʏᴏᴜʀ ᴜʀʟ", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)

