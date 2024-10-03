# esila sohbet
#@EsilaChatBot
# Sahib @debubluman
# repo
# Ropo

from AylinRobot import AylinRobot as app
from pyrogram import filters
from AylinRobot.config import Config
import os, youtube_dl, requests, aiohttp, wget, time, yt_dlp, lyricsgenius
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message, User
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message, CallbackQuery
)


@app.on_message(filters.command(["zxq"]))
async def lyrics(_, message: Message):
    m = await message.delete()  
    if len(message.command) < 2:
        return await message.reply_text("**İstifadə:**\n\n/zxq [ Şarkı İsmi]")
    m = await message.reply_text("✍️ şarkı sözleri aranıyor")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("şarkı sözleri bulunmadı: 🥹")
    xxx = f"""
**🙋‍♀️ İndirdi {Config.BOT_USERNAME}**
**🎶 Aranan Şarkı:-** __{query}__
 **📖 bulunmuş şarkı sözleri:-** __{S.title}__
 **✍️ Ressam:-** {S.artist}
 **📄 __Şarkı sözleri:__**

{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**Sözlər çox olduğundan fayl edib atdım...:**\n\n`zxk`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)
