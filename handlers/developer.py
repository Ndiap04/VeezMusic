import os
import re
import sys
import shutil
import traceback
import subprocess
from io import StringIO
from time import time
from pyrogram import Client, filters
from inspect import getfullargspec
from sys import version as pyver
from config import BOT_USERNAME
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


async def edit_or_reply(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})


