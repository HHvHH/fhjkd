from telethon import events, Button
from R0R77 import R0R77, BOT_USERNAME

btn =[
    [Button.inline("الادمن", data="admin"),],
    [Button.inline("التشغيل", data="play"), Button.inline("المحذوفين", data="zombies")],
    [Button.inline("الايدي", data="misc"),],
    [Button.inline("القائمة الرئيسية", data="start")]]

HELP_TEXT = "اهلا بك في قائمة اوامر البوت"


@R0R77.on(events.NewMessage(pattern="الاوامر"))
async def help(event):

    if event.is_group:
       await event.reply("اضغط على الاسفل لعرض الاوامر", buttons=[
       [Button.url("اضغط هنا", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@R0R77.on(events.NewMessage(pattern="^/start help"))
async def _(event):

    await event.reply(HELP_TEXT, buttons=btn)

@R0R77.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)
