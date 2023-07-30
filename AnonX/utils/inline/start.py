from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from SankiMusic.utilities.config import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="≽ ᴄᴏᴍᴍᴀɴᴅs ≼",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="✮ sᴇᴛᴛɪɴɢs ✮", callback_data="settings_helper"
            )
        ],
     ]
    return buttons

#extra shit
BOT_USERNAME = ("{BOT_USERNAME}")

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ᴜᴘᴅᴀᴛᴇs ✭", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="✭ sᴜᴘᴘᴏʀᴛ ✭", url=config.SUPPORT_GROUP
            )
        ]
     ]
    return buttons
