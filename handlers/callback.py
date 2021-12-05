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

#MulaiPermainan

@Client.on_callback_query(filters.regex("cbmulai"))
async def cbmulai(_, query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "💨 Download", url=f"https://t.me/RessoMusicRobot?start=Z2V0LTQyMDczNDg3NzQ2ODM2"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}!\n\n 👌Kamu hanya bisa menggunakan mengunduh lagu,\n\n⚡ Untuk bisa mengunduh video Kalian bisa Dibot langsung,atau klik tombol dibawah!"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )
