from R0R77 import R0R77, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
• أهلا بك عزيزي في بوت الحماية وتشغيل الاغاني في المحادثة الصوتيه

- أستطيع تشغيل الاغاني في المحادثه الصوتيه بسرعة وجودة عاليه
- لدي بعض اوامر بوتات الحماية

• لمعرفة الاوامر أضغط على زر : الاوامر
"""

@R0R77.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("أضفني الى مجموعتك", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("Hasoni Alnajar", f"https://t.me/hsshh"), Button.url("Ch", f"https://t.me/hasoni_lq")],
        [Button.inline("الاوامر", data="help")]])
       return

    if event.is_group:
       await event.reply("**- اهلا بك انا اعمل بنجاح**")
       return



@R0R77.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("أضفني الى مجموعتك", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("Hasoni Alnajar", f"https://t.me/hsshh"), Button.url("Ch", f"https://t.me/hasoni_lq")],
        [Button.inline("الاوامر", data="help")]])
       return
