from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import OWNER_ID, BOT_STATS_TEXT
from datetime import datetime
from helper_func import get_readable_time
from database.database import present_admin

@Bot.on_message(filters.command('stats'))
async def stats(bot: Bot, message: Message):
    user_id = message.from_user.id
    is_admin = await present_admin(user_id)
    
    if user_id != OWNER_ID and not is_admin:
        return
    
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))

        
