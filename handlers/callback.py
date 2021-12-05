# (C) 2021 VeezMusic-Project

from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
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

@Client.on_callback_query(filters.regex("cbmulai"))
async def cbmulai(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""⛔ **Peringatan Untuk Anda!**

🙇 Dimohon Untuk Tidak Menghapus Pesan Ketika Game Sedang Berlangsung!
Ketika Kamu Sudah Mencapai PDKT2 Dan Seterusnya Dan Kamu Menghapus Pesan Nya 
Kamu Akan Mengulang Dari Awal Kembali!

👨 Ketika Kamu Ingin Beristirahat Kamu Keluar Dari Bot Saja Jangan Menghapus Pesannya
Kirim Donasi Jika Anda Terlanjur Menghapus Pesannya Dan Ingin Melanjutkannya!**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✓ Setuju Dan Lanjutkan", callback_data="cbpdkt")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbpdkt"))
async def cbpdkt(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**PDKT**

Tahun ini merupakan tahun terakhir loh di
SMA. dan loh berniat untuk ngewujudin
impian loh semua yang belum tercapai,
yaitu jadian sama **Sabrina**, cewek cantik tapi judes
yang loh taksir sejak dulu.
**Berhasil Loh Dapatin Sabrina?**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbhelp")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbpdkt1"))
async def cbpdkt1(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""hi

Kirim Donasi Jika Anda Terlanjur Menghapus Pesannya Dan Ingin Melanjutkannya!**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )
