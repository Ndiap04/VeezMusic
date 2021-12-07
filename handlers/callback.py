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

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

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
        f"""😮 **Rendi** : __Hmm... Dimana Nih...__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbbella")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbbella"))
async def cbbella(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😀 **Rendi** : __Oh iya ini dikamar gua. Gua harus cepat kesekolah buat ketemu sama sih sabrina__!""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsisil")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsisil"))
async def cbsisil(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🤖 : **Loh bergegas mengganti baju tidur loh, dengan baju seragam kesekolah loh**...""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsilvi")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsilvi"))
async def cbsilvi(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😰 **Rendi** : __Fuhh... Sampe Juga... untung gak telat.__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsalsa")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsalsa"))
async def cbsalsa(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😦 **Rendi** : __Wahh itu dia sih Sabrina__....""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbfalah")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbfalah"))
async def cbfalah(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😨 **Rendi** : __Mesti Cepat Gua samperin nih__...""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbfilden")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbfilden"))
async def cbfilden(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👨 **Rendi** : .....""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Menyapanya", callback_data="cbhelp")],
                [InlineKeyboardButton("Sok Kenal", callback_data="cbdewi")],
                [InlineKeyboardButton("Pura² Salah Orang", callback_data="cbhelp")],
                [InlineKeyboardButton("Pura-Pura Menabraknya", callback_data="close")],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cbdewi"))
async def cbdewi(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😀 **Rendi**: __Hai...Ini Sabrina Anak IPA 1 kan?__...""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbferi")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbferi"))
async def cbferi(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😦 **Sabrina** : __Iya,Kenapa?__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsakinah")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsakinah"))
async def cbsakinah(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😅 **Rendi** : __Ehhh...Gpp ko,Salam kenal ya!__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cblinda")]]
        ),
    )

@Client.on_callback_query(filters.regex("cblinda"))
async def cblinda(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😬 **Sabrina** : ......""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbfredi")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbfredi"))
async def cbfredi(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😏 **Sabrina** : __Iya...Lam kenal juga.__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbamal")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbamal"))
async def cbamal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😣 **Rendi** : __(gile..nih cewe jutek banget)__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbriyan")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbriyan"))
async def cbriyan(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😶 **Rendi** : __(Gua Harus Nyari Topik...Biar Bisa Ngobrol Terus Bareng Dia)__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbdapur")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbdapur"))
async def cbdapur(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👨 **Rendi** : .....""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Loh Tinggal Dimana?", callback_data="cbsendok")],
                [InlineKeyboardButton("Sok Kenal", callback_data="cbdewi")],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cbsendok"))
async def cbsendok(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😀 **Rendi** : __Loh Tinggal Dimana?__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbrumah")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbrumah"))
async def cbrumah(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😑 **Sabrina** : __Dirumah.__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbalamat")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbalamat"))
async def cbalamat(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👨 **Rendi** : .....""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Aduh Pinter Banget", callback_data="cbpinter")],
                [InlineKeyboardButton("Ya Tau.Tapi Dimana Alamat nya?", callback_data="cbdewi")],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cbpinter"))
async def cbpinter(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😀 **Rendi** : __Aduh Pinter Banget__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbpede")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbpede"))
async def cbpede(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😁 **Sabrina** : __Makasih..Emang gua pinter!__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbbijak")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbbijak"))
async def cbbijak(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👨 **Rendi** : .....""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Ko Lu Pede Banget?", callback_data="cbbabi")],
                [InlineKeyboardButton("udah gitu cantik lagi hehehe", callback_data="cbdewi")],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cbbabi"))
async def cbbabi(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😁 **Rendi** : __Ko Lu Pede Banget?__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbmasalah")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbmasalah"))
async def cbmasalah(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😤 **Sabrina** : __Dihh,Kenapa Masalah buat loh?__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbgalak")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbgalak"))
async def cbgalak(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😁 **Rendi** : __Ehhh...gua bercanda ko , ko lu galak gitu sih.__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbtembok")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbtembok"))
async def cbtembok(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😠 **Sabrina** : __Tuh..gua malah dikatain lagi!__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsingkong")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsingkong"))
async def cbsingkong(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👨 **Rendi** : .....""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Pagi Pagi Jangan Marah² dong", callback_data="cbdong")],
                [InlineKeyboardButton("iya iya maaf", callback_data="cbdewi")],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cbdong"))
async def cbdong(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😀 **Rendi** : __Pagi Lagi Jangan Marah² dong, nanti cantik nya ilang loh!__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsinga")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsinga"))
async def cbsinga(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😑 **Sabrina** : .....""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbnama")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbnama"))
async def cbnama(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😀 **Sabrina** : __hahaha iya deh....btw nama lu siapa?__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbmusang")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbmusang"))
async def cbmusang(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😁 **Rendi** : __Gua Rendi dari IPA 5...__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbkodok")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbkodok"))
async def cbkodok(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😊 **Rendi** : __btw sendirian aja sab?__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbkatain")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbkatain"))
async def cbkatain(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😊 **Sabrina** : __Iya lah..kan berangkat nya sendiri.__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbjengkol")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbjengkol"))
async def cbjengkol(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👨 **Rendi** : .....""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Btw loh cantik banget ya Sab", callback_data="cbdong")],
                [InlineKeyboardButton("Lain kali bareng aja", callback_data="cbguru")],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cbguru"))
async def cbguru(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😊 **Rendi** : __Lain kali bareng aja sama gua..__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbnaik")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbnaik"))
async def cbnaik(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😀 **Sabrina** : __Emg biasanya loh naik apa?__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbkuxa")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbkuxa"))
async def cbkuxa(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👨 **Rendi** : .....""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("naik angkot", callback_data="cbangkot")],
                [InlineKeyboardButton("Jalan Kaki", callback_data="cbjalan")],
                [InlineKeyboardButton("bawa motor", callback_data="cbbus")],
                [InlineKeyboardButton("bawa mobil", callback_data="cbtruck")],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cbjalan"))
async def cbjalan(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😁 **Rendi** : __Jalan Kaki Sab.__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbsory")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsory"))
async def cbsory(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😄 **Sabrina** : __Duhh... Sory Ya,tiba tiba perut gua mules nih.
Gu pergi dulu ya.bye!__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbngacir")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbngacir"))
async def cbngacir(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🤖 : **SABRINA LANGSUNG NGACIR NINGGALIN LOH.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbbicit")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbbicit"))
async def cbbicit(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😭😭😭😭😭😭😭😭😭😭😭😭
**BARU SAMPE** : PDKT 1""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Coba Lagi", callback_data="cbsilvi")],
                [InlineKeyboardButton("Nyerah", callback_data="close")],
            ]
        ),
    )
