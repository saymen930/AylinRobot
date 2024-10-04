## Sahib 

import logging, asyncio, random
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from AylinRobot.config import Config
from Telethon.Mesajlar import soz, emoji, bayrak

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)
 
api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []
 
ozel_list = [2074934667]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}
	
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**etiket durduruldu**\n\n📊 **etiketlenenlerin sayısı:** `{rxyzdev_tagTot[event.chat_id]}`")
 

@client.on(events.NewMessage(pattern='^.dur ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**etiket işlemi durduruldu.**\n\n📊 **etiketlenenlerin sayısı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
	
@client.on(events.NewMessage(pattern="^.tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ özel de etiket Olmaz**\n**✅ Bu komut Sadece Qruplarda Ve Kanallarda Geçerlidir!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Sen Admin Degilsin bebek!**\n✅ Bu komut Sadece Adminler için Geçerlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Geçmiş Mesajlar İçin Kullanıcılardan Talep Almıyorum❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 etiket yapa Bilmem için bana Metin Ver**")
  else:
    return await event.respond("**❌ etiket atmam için bir sebeb Yok\n✅ etiket yapa Bilmem için bana Metin Ver\nℹ `/tag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Etiket işlemi Başlatıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ etiket işlemi Tamamlandı !.\n\n📊 etiketlenenlerin Sayısı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ etiket işlemi Tamamlandı !.\n\n📊 etiketlenenlerin Sayısı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")


@client.on(events.NewMessage(pattern="^.ttag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("*❌ özel De etiket Olmaz**\n**✅ Bu komut Sadece Qruplarda Ve Kanallarda Geçerlidir!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("** ⛔ Sen Admin Deyilsin!**\n✅ Bu komut Sadece Qruplarda Ve Kanallarda Geçerlidir**")
 
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("***🔗 Geçmiş Mesajlar İçin Kullanıcılardan Talep Almıyorum❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver!**")
  else:
    return await event.respond("**❌ etiket atmam için Bir Sebeb Yok\n✅ etiket ata Bilmem için Sebeb Yazın\nℹ `/ttag Selam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Etiketleme işlemi Başlatıldı.!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n📢 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ etiket işlemi Tamamlandı !.\n\n📊 Etiketlenenlerin Sayısı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 etiketi Başlatan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n📢 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ etiket işlemi Tamamlandı !.\n\n📊 Etiketlenenlerin Sayısı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 etiketi Başlatan: {rxyzdev_initT}**")
 
 
 
@client.on(events.NewMessage(pattern="^.stag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("*❌ özel De etiket Olmaz**\n✅ Bu komut Sadece Qruplar Ve Kanllar için Geçerlidir.")
  
  admins = []
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("⛔ **Sen Admin Deyilsin!**\n✅ **Bu komut Sadece Adminler Üçün Geçerlidir**")
 
  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("ℹ **bak tepem atyor artık yapma**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Bir Mesajı Yanıtlayın Yada etiket ata Bilmem için Bir Sebeb Yazın\n✅ Örnek:-`/etag Selam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi Başlatıldı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"*✅ etiket işlemi Tamamlandı**\n\n**📊 Etiketlenenlerin Sayısı:-**  `{rxyzdev_tagTot[event.chat_id]}`\n**👤 işlemi Başlatan:-** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ etiket işlemi Tamamlandı**\n\n**⚡ Etiket Atıldı:-**  `{rxyzdev_tagTot[event.chat_id]}`\n**🗣 işlemi Başlatan:-**  {rxyzdev_initT}")
 
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Etiket işlemi Durduruldu.**\n\n📋 **Etiketlenenlerin Sayısı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern="^.etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ Özel de Olmaz**\n**✅ Bu komut Sadece Qruplar Ve Kanallar için Geçerlidir!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Sen Admin Degilsin!**\n✅ Bu komut Sadece Adminler için Geçerlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Kafanı kıracam yapma❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Etiket Atmak İçin Bir Sebeb Yok\n✅ Etiket Ata Bilmm İçin Sebeb Yazın\nℹ `/etag Selam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Etiket İşlemi Başlatıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"- [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Etiketlenenlerin sayısı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f" - [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket İşlemi Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Etiket İşlemi Durduruldu.**\n\n📊 **Etiketlenenlerin sayısı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 


@client.on(events.NewMessage(pattern="^.rtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM De Etiket Olmaz**\n**✅ Bu Komut Sadece Qruplarda Və Kanallarda Geçerlidir!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Sen Yönetici Deyilsin!**\n✅ Bu Komut Sadece Yöneticiler İçin Geçerlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Geçmiş Mesajlar İçin Kullanıcılardan Bahs Edemem❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Etiket Atmam İçin Banan Metin Ver**")
  else:
    return await event.respond("**❌ Etiket Atmak İçin Bir Sebeb Yok\n✅ Etiket Atmam İçin Sebeb Yazın\nℹ `/rtag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Etiket işlemi Başladı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket İşlemi Başarıyla Tamamlandı !.\n\n📊 Etiketlenlerin Sayısı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Etiketi Başlatan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket İşlemi Başarıyla Tamamlandı !.\n\n📊 Etiketlenlerin Sayısı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Etiketi Başlatan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Etiket İşlemi Durduruldu.**\n\n📊 **Etiketlenlerin Sayısı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
 

@client.on(events.NewMessage(pattern="^.btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM De Etiket Olmaz**\n**✅ Bu Komut Sadece Yöneticiler İçin Geçerlidir!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Yönetici değilsiniz!**\n✅ Bu Komut Sadece Yöneticiler İçin Geçerlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Geçmiş Mesajlar İçin Kullanıcılardan Bahsedemem❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Etiket Ata Bilmem İçin Bana metni ver**")
  else:
    return await event.respond("**❌ Etiket Atmak İçin Bir Sebeb Yok\n✅ Etiket Ata Bilmem İçin Sebeb Yazın\nℹ `/btag Selam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Etiket İşlemi Başlatıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"- [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi Tamamlandı !.\n\n📊 etiketlenenlerin Sayısı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 işlemi Başlatan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f" - [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi Tamamlandı !.\n\n📊 etiketlenenlerin Sayısı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 işlemi Başlatan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Etiket işlemi durduruldu.**\n\n📊 **etiketlenenlerin Sayısı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
		


@client.on(events.NewMessage(pattern="^.admin ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "♕︎ Qrup Adminlərinin Listesi ♕︎\n\n"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n ➪ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation
    
    
    
    
SAHIB = Config.OWNER_ID

@client.on(events.NewMessage(pattern="^.pin ?(.*)"))
async def pin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("🗨 Lütfen Bir Mesaja Yanıt Verin")
        await event.reply("📌 aşko Mesajın sabitlendi!")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} Bota Sahib Degilsin!\n⛔ Yapma saçını başını yolarım.")
 

@client.on(events.NewMessage(pattern="^.unpin ?(.*)"))
async def unpin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("🗨 lütfen sabitlenmiş  Mesaja Yanıt Ver")
        await event.reply("Sahibim Pinlənmiş Mesaj Qaldırıldı")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} Bota Sahib Degilsin!\n⛔  dur yapma.")    
        





@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))


@client.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Hmm")

userjoin = (

    "hoş Geldin",
    "hoş geldin Güzel İnsan", 
    "Senin Gelişin beni Sevindirdi", 
    "Aramıza hoş Geldin",
    "Aşkolar toplandık parti yapıyoruz hoşgeldin",
    "Uzun zamandır seni bekliyorum nerdasın",
    "hoşgeldin, seni aramızda gördüğümüz için çok mutluyuz... Ne duruyorsun hadi sohbete katılsana ☺️☺️.",
    "Hoşgeldin, gideceksen şimdiden git 😒.",
)




@client.on(events.NewMessage(pattern=f'@{Config.OWNER_NAME}'))
@client.on(events.NewMessage(pattern='Huseyn'))
@client.on(events.NewMessage(pattern='@Hesenov_H'))
@client.on(events.NewMessage(pattern='Husi'))
async def handler(event):
    await event.reply(random.choice(Aylin))



Aylin = (
    "😒 Benim bebeğimi az etiketle",
    "🤭 Hmm Benim Sahibimle Nə İşin Var?",
    "😖 Git Uyu",
    "🚷 Ban Yedin !\nSebeb: Sahibimi etiketlediğin için \nŞaka ya korkma 😂",
    "Burda olmasada kalbi sizinle ❤️",
)
