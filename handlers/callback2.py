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

@Client.on_callback_query(filters.regex("cbpdkt11"))
async def cbpdkt11(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😦 : Wahh itu dia sih Sabrina....""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbpdkt12")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbpdkt12"))
async def cbpdkt12(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""😨 : Mesti Cepat Gua samperin nih...""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Lanjutkan", callback_data="cbpdkt13")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbpdkt13"))
async def cbpdkt13(_, query: CallbackQuery):
    await query.edit_message_text(
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
