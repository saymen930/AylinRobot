# 
# 
# Repo 

import aiohttp
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters


@app.on_message(filters.command("github"))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/github Kullanıcı adınızı yazmadınız 😐")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")
            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']
                caption = f"""**Info Of {name}**
👨🏻‍💻Kullanıcı Adı: {username}
🗣️Bio: {bio}
🔗Profil linki: [Here]({url})
👤Şirket: {company}
📅Oluşum Tarihi: {created_at}
📔Depolar: {repositories}
🛄Blog: {blog}
🌐Mekan: {location}
👁️‍🗨️İzleyicilər: {followers}
👁️‍🗨️Takip ettikleri: `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)
