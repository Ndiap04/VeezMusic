from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    ALIVE_IMG,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Halo Masbro {message.from_user.mention()} !**\n

💡 **Silakan Mulai Permainan Untuk Memulai Game Nya , Klik Help Untuk Mendapatkan Bantuan**!

© Powered By : [Sukses Makmur](http://t.me/SuksesMakmur)**""",
        reply_markup=InlineKeyboardMarkup(
                        [ 
                [
                    InlineKeyboardButton(
                        "🙎‍♂ Mulai Bro 🙍‍♀", callback_data="cbmulai"),
                ],[
                    InlineKeyboardButton(
                        "📩 Kontak Developer", callback_data="cbkontak"
                    ),
                    InlineKeyboardButton(
                        "💌 Tentang Bot ini", callback_data="cbinfo")
                ],[
                    InlineKeyboardButton(
                        "📝 Komentar", callback_data="cbkomen"
                    ),
                    InlineKeyboardButton(
                        "🎉 Bantuan", callback_data="cbhelp")
                ],[
                    InlineKeyboardButton(
                        "❔ Update", callback_data="cbupdate"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(
    command(["play_pdkt", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def play_pdkt(client, message):
    await client.send_photo(message.chat.id,
        photo=f"{ALIVE_IMG}",
        caption=f"""**Hi**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "Updates", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )
