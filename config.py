#Made by SahilXCodes 
#Telegram - @Its_Sahil_Ansari

import os
import logging
from logging.handlers import RotatingFileHandler

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6700290832:AAHmoKLOK2U4zLrpXPmgBiZSk7WZ5c2-U5o") #Bot Token
APP_ID = int(os.environ.get("APP_ID", "23539392")) #API_ID
API_HASH = os.environ.get("API_HASH", "5ee767ace3c694a4fb39cdd2cc78eaca") #Telegram HASH

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

OWNER_ID = int(os.environ.get("OWNER_ID", "1576425650"))  # OWNER ID

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Yuuichi:Yuuichi@cluster0.plcnxqv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Yuuichi")

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002048004827")) #Logs channel id for files

##--------------------------------------------------------------------------------------------------------------------------------------------

#If you don't want forcesub then leave blank
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1002459794646")) #Forcesub1
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1002290873966")) #Forcesub2

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/90a5b40870306cc1cabf3-7007ef66625077cc0e.jpg") #Telegraph Image with for start Message
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/5136fba2eedc5e1799d2e-e4b2c3bf0dd1ed47dd.jpg") #Telegraph Image with for Forcesub Message

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

HELP_TXT = "<b><blockquote>1. First Join the channel\n2. Tap on Original link again or Reload ⚡️\n3. Tap on Start and Done ✅</blockquote></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>ʜɪ ᴛʜᴇʀᴇ... {mention}</blockquote>! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\n<a href=https://t.me/Cultured_Oasis>ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴏᴛᴛ ᴏʀɪɢɪɴᴀʟꜱ<a></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<blockquote>›› ʜᴇʏ {mention} ×</blockquote>\n ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs")
CMD_TXT = "<b><blockquote>× ᴄᴏᴍᴍᴀɴᴅꜱ ꜰᴏʀ ᴀᴅᴍɪɴꜱ ×</blockquote>\n\n/start - Start the bot or get posts\n/batch - Create links for multiple posts\n/nbatch - Advanced batch processing\n/genlink - Create link for one post\n/users - View bot statistics\n/broadcast - Broadcast messages to users\n/stats - Check bot uptime\n/add_admin - Add admins\n/del_admin - Remove admins\n/admins - View admin list\n/forcesub1 - Change ForceSub Channel 1\n/forcesub2 - Change ForceSub Channel 2\n/viewforce - View ForceSub channels</b>"
##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

AUTO_DEL = os.environ.get("AUTO_DEL", "True") #TRUE/FALSE
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600")) #Seconds
DEL_MSG = "<b><blockquote>Yᴏᴜʀ ғɪʟᴇs ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴡɪᴛʜɪɴ 10 Mɪɴᴜᴛᴇs. Sᴏ ᴘʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜᴇᴍ ᴛᴏ ᴀɴʏ ᴏᴛʜᴇʀ ᴘʟᴀᴄᴇ ғᴏʀ ғᴜᴛᴜʀᴇ ᴀᴠᴀɪʟᴀʙɪʟɪᴛʏ.</blockquote></b>"

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

#Don't change anything
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}</b>"

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

#Don't change anything
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

#Don't change anything
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
PORT = os.environ.get("PORT", "7011")

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------

#Don't change anything
LOG_FILE_NAME = "file-sharing.txt"
LOG_FILE_NAME = "file-sharing.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

##--------------------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------------------    

#Bhen ke lavdo Credit hataya na ma choddunga wahi aakr salo use karo bas 
