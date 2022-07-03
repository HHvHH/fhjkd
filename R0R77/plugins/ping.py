import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/7e896dba43e7e25106e4e.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@HssHH"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("Hasoni Alnajar", "https://t.me/hsshh")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
