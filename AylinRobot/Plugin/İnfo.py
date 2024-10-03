# 
# 
# 

import os, asyncio, time, shlex, requests, pyrogram
from helpers.extract_user import extract_user, last_online
from datetime import datetime
from AylinRobot import AylinRobot as app
from pyrogram import filters, Client
from AylinRobot.config import Config



@app.on_message(filters.command("info"))
async def info(client, message):
    """ Kullanıcı bilgilerini çıkarın """
    status_message = await message.reply_text(
        "🔎"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        await status_message.edit("Geçerli Kullanıcı_ID / gösterilmedi 🙄")
        return
    
    first_name = from_user.first_name or ""
    last_name = from_user.last_name or ""
    username = from_user.username or ""
    
    message_out_str = (
        "<b>Telegram verilənlər bazasından</b>\n\n"
        f"<b>• İsim : <a href='tg://user?id={from_user.id}'>{first_name}</a></b>\n"
        f"<b>• ID :</b> <code>{from_user.id}</code>\n"
        f"<b>• Kullanıcı Adı :</b> @{username}\n"
        f"<b>• Link :</b> {from_user.mention}\n" if from_user.username else ""
        f"<b>Silindi:</b>Doğrudur\n" if from_user.is_deleted else ""
        f"<b>Doğrulandı:</b>Doğrudur" if from_user.is_verified else ""
        f"<b>yalan:</b>Doğrudur" if from_user.is_scam else ""
        # f"<b>Is Fake:</b> True" if from_user.is_fake else ""
        f"<b>Son görülme:</b> <code>{last_online(from_user)}</code>\n\n"
    )

    if message.chat.type in ["supergroup", "channel"]:
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = datetime.fromtimestamp(
                chat_member_p.joined_date or time.time()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>• Lastseen :</b> <code>"
                f"{joined_date}"
                "</code>\n"
                "▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            caption=message_out_str,
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        await message.reply_text(
            text=message_out_str,
            quote=True,
            disable_notification=True
        )
    await status_message.delete()
