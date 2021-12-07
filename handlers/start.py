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
    START_IMG,
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
async def start(client, message):
    await client.send_photo(message.chat.id,
        photo=f"{START_IMG}",
        caption=f"""**Halo MashBro!!** {message.from_user.mention()} !**\n

/playfree_pdkt_kkcdc (Playing Game)

© Powered By : [Sukses Makmur](http://t.me/SuksesMakmur)**""",
        reply_markup=InlineKeyboardMarkup(
                        [ 
                [
                    InlineKeyboardButton(
                        "🙎‍♂ Donasi Untuk Developer 🙍‍♀", callback_data="cbgaktau"),
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
    command(["playfree_pdkt_kkcdc", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def playfree_pdkt_kkcdc(client, message):
    await client.send_photo(message.chat.id,
        photo=f"{ALIVE_IMG}",
        caption=f"""**PDKT 1**

Tahun ini merupakan tahun terakhir loh 
di SMA. dan loh berniat untuk ngewujudin
impian loh semua yang belum tercapai,
yaitu jadian sama Sabrina, cewek cantik tapi judes
yang loh taksir sejak dulu.
Berhasil Loh Dapatin Sabrina?""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Mainkan", callback_data="cbsabrina")]]
        ),
    )
