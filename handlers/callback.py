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
        f"""**PDKT 1**

Tahun ini merupakan tahun terakhir loh 
di SMA. dan loh berniat untuk ngewujudin
impian loh semua yang belum tercapai,
yaitu jadian sama **Sabrina**, cewek cantik tapi judes
yang loh taksir sejak dulu.
**Berhasil Loh Dapatin Sabrina?**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Mulai Permainan", callback_data="cbsabrina")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsabrina"))
async def cbsabrina(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Selamat Datang Dimasa Depan,
Loh Adalah Seorang Time Traveler!**

**Artinya Lo punya kemampuan Khusus untuk kembali ke masa lalu**

**Dengan Kemampuan Khusus Ini Loh Berulang Kali Kembali Dari Masa Depan....**

**Untuk Mendapatkan Hati Pujaan loh si Sabrina.**

**Semoga Kali Ini Bisa Berhasil Ya Bro!**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsendi")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsendi"))
async def cbsendi(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😮 : Hmm... Dimana Nih...""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbbella")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbbella"))
async def cbbella(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😀 : Oh iya ini dikamar gua. Gua harus cepat kesekolah buat ketemu sama sih sabrina!""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsisil")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsisil"))
async def cbsisil(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Loh bergegas mengganti baju tidur loh, dengan baju seragam kesekolah loh...""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsilvi")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsilvi"))
async def cbsilvi(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😰 : Fuhh... Sampe Juga... untung gak telat.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsalsa")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsalsa"))
async def cbsalsa(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😦 : Wahh itu dia sih Sabrina....""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbfalah")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbfalah"))
async def cbfalah(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😨 : Mesti Cepat Gua samperin nih...""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbfilden")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbfilden"))
async def cbfilden(_, query: CallbackQuery):
    await query.edit_Message_text(
        f"""ㅤㅤㅤㅤ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Menyapanya", callback_data="cbhelp")],
                [InlineKeyboardButton("Sok Kenal", callback_data="cbhelp")],
                [InlineKeyboardButton("Pura² Salah Orang", callback_data="cbhelp")],
                [InlineKeyboardButton("Pura² Menabraknya", callback_data="close")],
            ]
        ),
    )
