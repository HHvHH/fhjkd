import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/16c8c27938bc7ac235436.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@HvvHH"
)

CAPTION = f"**سرعة البنق :** {ms}"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("Haider .", "https://t.me/HvvHH")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
