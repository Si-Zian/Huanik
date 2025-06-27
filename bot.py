import asyncio
from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
from datetime import datetime, timedelta
from database.database import present_channel, present_channel2
import pyrogram.utils
import sys
import logging
from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, CHANNEL_ID, PORT

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )

        # ✅ Logger Setup - Sirf Warnings & Errors Print Honge
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(message)s",
            level=logging.WARNING
        )
        self.LOGGER = logging.getLogger("Bot").warning

        self.invitelink1 = None
        self.invitelink2 = None
        self.FORCESUB_CHANNEL = None
        self.FORCESUB_CHANNEL2 = None

    async def start(self, *args, **kwargs):
        await super().start(*args, **kwargs)
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        await self.update_forcesub_channels()

        if self.FORCESUB_CHANNEL or self.FORCESUB_CHANNEL2:
            asyncio.create_task(self.auto_revoke_invite_links())

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(f"Bot is not admin in DB channel. Error: {e}")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER("Bot Running...!")
        self.username = usr_bot_me.username

        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def update_forcesub_channels(self):
        """Fetches latest FORCESUB_CHANNEL values and revokes old links if changed."""
        new_channel1 = await present_channel()
        new_channel2 = await present_channel2()

        changed = False  

        if new_channel1 != self.FORCESUB_CHANNEL:
            if self.invitelink1:
                try:
                    await self.revoke_chat_invite_link(self.FORCESUB_CHANNEL, self.invitelink1)
                except Exception as e:
                    self.LOGGER(f"Error revoking invite link 1: {e}")
            self.FORCESUB_CHANNEL = new_channel1
            changed = True

        if new_channel2 != self.FORCESUB_CHANNEL2:
            if self.invitelink2:
                try:
                    await self.revoke_chat_invite_link(self.FORCESUB_CHANNEL2, self.invitelink2)
                except Exception as e:
                    self.LOGGER(f"Error revoking invite link 2: {e}")
            self.FORCESUB_CHANNEL2 = new_channel2
            changed = True

        if changed:
            await self.generate_temporary_invite_links()

        await asyncio.sleep(10)
        asyncio.create_task(self.update_forcesub_channels())

    async def generate_temporary_invite_links(self):
        """Generates fresh invite links based on the latest channel IDs."""
        try:
            expire_time = datetime.now() + timedelta(minutes=10)

            if self.FORCESUB_CHANNEL:
                invite = await self.create_chat_invite_link(
                    self.FORCESUB_CHANNEL, 
                    creates_join_request=False, 
                    expire_date=expire_time
                )
                self.invitelink1 = invite.invite_link

            if self.FORCESUB_CHANNEL2:
                invite = await self.create_chat_invite_link(
                    self.FORCESUB_CHANNEL2, 
                    creates_join_request=False, 
                    expire_date=expire_time 
                )
                self.invitelink2 = invite.invite_link

        except Exception as e:
            self.LOGGER(f"Error while generating invite links: {e}")

    async def auto_revoke_invite_links(self):
        """Revokes and generates new invite links every 10 minutes."""
        while True:
            await asyncio.sleep(600)
            await self.update_forcesub_channels()

            if self.invitelink1 and self.FORCESUB_CHANNEL:
                try:
                    await self.revoke_chat_invite_link(self.FORCESUB_CHANNEL, self.invitelink1)
                except Exception as e:
                    self.LOGGER(f"Error revoking invite link 1: {e}")

            if self.invitelink2 and self.FORCESUB_CHANNEL2:
                try:
                    await self.revoke_chat_invite_link(self.FORCESUB_CHANNEL2, self.invitelink2)
                except Exception as e:
                    self.LOGGER(f"Error revoking invite link 2: {e}")

            await self.generate_temporary_invite_links()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER("Bot stopped.")