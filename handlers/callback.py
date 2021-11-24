# (C) 2021 VeezMusic-Project

from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome {message.from_user.mention()} !**\n
💭 **Kirimkan nama artis dan/atau nama lagu dan saya akan mencarikan musik untuk kamu!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
               [
                InlineKeyboardButton(
                    "Perintah", callback_data="close",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Perintah**

Kirimkan nama artis dan/atau nama lagu dan saya akan mencarikan musik untuk kamu!

/song (nama lagu) - cari berdasarkan judul lagu
/artis (nama artis) - cari berdasarkan nama artis
/lyrics (nama lagu) - cari berdasarkan judul lagu

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )
