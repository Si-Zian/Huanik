#Made by SahilXCodes 
#Telegram - @Its_Sahil_Ansari

from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from config import OWNER_ID
from database.database import present_admin, add_admin, full_adminbase, del_admin

#-------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------

@Bot.on_message(filters.command("add_admin"))
async def add_admin_command(client: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("Only the Owner can use this command, sorry!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>You're using the wrong format. Please use it like this:</b> /add_admin {user_id}")
        return

    try:
        admin_id_add = int(message.command[1])
        user_info = await client.get_users(admin_id_add)
    except ValueError:
        await message.reply_text("Invalid user ID. Please check again!")
        return

    first_name = user_info.first_name
    last_name = user_info.last_name if user_info.last_name else "" 
    full_name = f"{first_name} {last_name}".strip()

    added = await add_admin(admin_id_add)
    if added:
        await message.reply_text(f"<b>{first_name} - {admin_id_add} is already an admin.</b>")
    else:
        await message.reply_text(f"<b>{first_name} - {admin_id_add} is now an admin.</b>")

#-------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------

@Bot.on_message(filters.command('del_admin'))
async def remove_admin_command(client: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("Only Owner can use this command...!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>You're using the wrong format. Please use it like this:</b> /del_admin {user_id}")
        return

    try:
        admin_id_remove = int(message.command[1])
        user_info = await client.get_users(admin_id_remove)  # Fetch user details
    except ValueError:
        await message.reply_text("Invalid user ID. Please check again...!")
        return

    first_name = user_info.first_name
    last_name = user_info.last_name if user_info.last_name else ""  # Last name could be None
    full_name = f"{first_name} {last_name}".strip()

    removed = await del_admin(admin_id_remove)
    if removed:
        await message.reply_text(f"<b>{first_name} - {admin_id_remove} was neither an admin nor found in the admin list.</b>")
    else:
        await message.reply_text(f"<b>{first_name} - {admin_id_remove} has been removed from the admin list.</b>")

#-------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------

@Bot.on_message(filters.command('admins'))
async def admin_list_command(client: Bot, message: Message):
    user_id = message.from_user.id

    if user_id != OWNER_ID:  # Ensuring type consistency
        await message.reply_text("🚫 Only the Owner can use this command!")
        return

    our_admin_ids = await full_adminbase()
    if not our_admin_ids:
        await message.reply_text("<b>⚠️ No admins found!</b>", disable_web_page_preview=True)
        return

    formatted_admins = []
    for admin_id in our_admin_ids:
        try:
            admin_id = int(admin_id)  # Ensure it's an integer
            user = await client.get_users(admin_id)
            full_name = f"{user.first_name} {user.last_name or ''}".strip()
            formatted_admins.append(f"🔹 {full_name} - <code>{admin_id}</code>")
        except Exception as e:
            print(f"⚠️ Skipping invalid admin_id: {admin_id} -> {e}")  # Debugging
            continue  # Skip invalid user

    if formatted_admins:
        admins_text = "\n".join(formatted_admins)
        await message.reply_text(f"<b>👑 List of Admins:</b>\n\n{admins_text}", disable_web_page_preview=True)
    else:
        await message.reply_text("<b>⚠️ No valid admins found!</b>", disable_web_page_preview=True)