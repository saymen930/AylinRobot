# 
# 
# 
# Repo 

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Selam {}**
║
║▻ 🙋‍♀️ Benim Adım  ️️️️️️🙎‍♀️ [{}](https://t.me/{}) Ben 
║▻ TR Türkçede Çok Özellikli 
║▻ 💌 Telegram Botuyum Becerilerimi Görmek İçin
║▻ `📚 yardım` Buttonuna Basın
╚═════════════════
👨‍💻 **Sahibim** ♒️ @{}

"""    
    HELP_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Selam {} 
║
║▻ 💁‍♀️ ️️️️️️ [{}](https://t.me/{})- Un  
║▻ 📚 Komutlar  Bunlar Aşağıdaki 
║▻ 🖲 Buttonlara Basarak istediyiniz
║▻ ✔️ Komut Hakkında Bilgi Ala Bilirsiniz 
╚═════════════════
"""

    GSTART_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Selam {} 
║
║▻ 💁‍♀️ ️️️️️️ [{}](https://t.me/{})
║
║▻ ❤️‍🔥 {}  grupun Da Güzel Çalışıyor  🥳
╚═════════════════
"""



### Bot Haqqında Ümumi Məlumat

    BH_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Selam {} 
║
║▻ 🙎‍♀️ [{}](https://t.me/{}) TR Türkçede Çox Özellikli Telegram Botudur...**
║
║▻ ✨ Bot Versiyon: v0.7.0
║▻ 🍀 Pyrogram Versiyon: 1.4.16
║▻ ✨ Python Versiyon: 3.11.1
║▻ ⚙️ Sunucu [Heroku](https://heroku.com)
║▻ 📆 Bot Lisans Tarihi `20.11.2022` 
╚═════════════════
╔═════════════════
║▻ **⚠️ Grubunuzda Çalışması için 
║▻ Sadece Yönetici Komutlarından 
║▻ 💬 Mesajları Sil'e 🚫 İzin Ver**
╚═════════════════
"""

    MUSIC_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /song 
║▻ 🧩 Örnek: /song Rei - Ah Canım Sevgilim
║▻ 📃 Açıklama: şarkı yükleniyor.
║
║▻ 🔮 Kullanım: /video
║▻ 🧩  Örnek:/video Rei - Ah Canım Sevgilim
║▻ 📃 Açıklama: Video yükleniyor.
║
║▻ 🔮 Istifadə: /lyrics 
║▻ 🧩 Örnek: /lyrics Rei - Ah Canım Sevgilim
║
║▻ 📃 Açıklama: şarkının sözlerini bulur.
╚═════════════════
"""

    TELEGRAPH_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /tgm
║▻ 📃 Açıklama: Fotoğraf, video və ya GIF göndererek link ala bilirsiniz.
╚═════════════════
"""

    SEHID_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /şehit 
║▻ 📃 Açıqlama:  Bu komutla size **Şehid** adları gönderecem
╚═════════════════
╔═════════════════
║▻ 🥀 **Allah bütün Şehitlerimize rahmət eylesin**
║▻ 🤲 Mekanları Cennet Olsun 
║▻ 😔 Başın sağolsun Vatan
║▻ 🇦🇿/TR Botta **3130** Şehit adı mevcud
╚═════════════════
""" 
    OYUN_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /zer
║▻ 📃 Açıklama: zər atar
║
║▻ 🔮 Kullanım: /top
║▻ 📃 Açıklama: top atar
║
║▻ 🔮 Kullanım: /bowling
║▻ 📃 Açıklama: bowling atar
║
║▻ 🔮 Kullanım: /ox
║▻ 📃 Açıklama: ox atar
║
║▻ 🔮 Kullanım: /jackpot
║▻ 📃 Açıklama: jackpot atar
║
║▻ 🔮 Kullanım: /basket
║▻ 📃 Açıklama: basket atar
╚═════════════════

╔═════════════════
║▻🆕️  Kelime-Oyununun komutları
║
║▻ 🔮 Kullanım: /oyun
║▻ 📃 Açıklama: Oyunu Başlatır
║
║▻ 🔮 Kullanım: /atla
║▻ 📃 Açıklama: zor sözler
║
║▻ 🔮 Kullanım: /dur
║▻ 📃 Açıklama: Oyunu durdurur
║
║▻ 🔮 Kullanım: /skor
║▻ 📃 Örnek: Her Bir Oyuncunun Derecesini Gösterir
╚═════════════════
"""

    EğLENCE_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /foto3 
║▻ 📃 Açıklama: Rastgele 16+ fotoğrafları Atar.
║
║▻ 🔮 Kullanım: /kedi
║▻ 📃 Açıklama: Rastgele kedi fotoğrafları Atar
║
║▻ 🔮 Kullanım: /anime
║▻ 📃 Açıklama: Rastgele Anime fotoğrafları Atar
║
║▻ 🔮 Kullanım: /araba
║▻ 📃 Açıklama: Rastgele Araba fotoğrafları Atar
║
║▻ 🔮 Kullanım: /araba2
║▻ 📃 Açıklama: Rastgele Araba fotoğrafları Atar
║
║▻ 🔮 kullanım: /tema
║▻ 📃 Açıklama: Rastgele Telegram Teması Atar
║
║▻ 🔮 Kullanım: /pp
║▻ 📃 Açıklama: Rastgele Profil fotoğrafları Atar
║
║▻ 🔮 Istifadə: /sevgi
║▻ 📃 Açıqlama: Hazır Sevgi Yə Aid Sözlər Atar.
║
║▻ 🔮 Istifadə: /bio
║▻ 📃 Açıqlama: Hazır Bio Nuz Üçün Sözlər Atar.
╚═════════════════
"""


    ELAVELER_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /id
║▻ 📃 Açıqlama: İstifadəçinin ID alın.
║
║▻ 🔮 Istifadə: /info
║▻ 📃 Açıqlama: İstifadəçi haqqında məlumat verər
║
║▻ 🔮 Istifadə: /alive
║▻ 📃 Açıqlama: Botun işlək olduğunu yoxlayar.
╚═════════════════
"""


    AXTARIS_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /github 
║▻ 🧩 Nümunə: /github HesenovHuseyn
║▻ 📃 Açıqlama: Github Axtarışı Edər.
║
║▻ 🔮 Istifadə: /search
║▻ 🧩 Nümunə: /search Rei - Ah Canım Sevgilim
║▻ 📃 Açıqlama: YouTube axtarış üçün istifadə edə bilərsiniz.
╚═════════════════
"""

    TAGGER_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /tag
║▻ 📃  Açıqlama: [Səbəb] - 5 - Li Tağ.
║
║▻ 🔮 Istifadə: /ttag
║▻ 📃  Açıqlama: [Səbıb] - Təkli Tağ.
║
║▻ 🔮 Istifadə: /stag
║▻ 📃  Açıqlama: Maraqlı Sözlərlə Tağ.
║
║▻ 🔮 Istifadə: /etag
║▻ 📃  Açıqlama: [Səbəb] - Emoji İlə Tağ.
║
║▻ 🔮 Istifadə: /btag
║▻ 📃  Açıqlama: [Səbəb] - Bayraqlarla Tağ
║
║▻ 🔮 Istifadə: /admin
║▻ 📃 Açıqlama: Adminlərin Toplu Siyahısı
╚═════════════════
"""

    SAHIB_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /stats
║▻ 📃 Açıqlama: Bot haqqında ümumi məlumat verər.
║
║▻ 🔮 Istifadə: /block
║▻ 📃 Açıqlama: İstifadəçini Və Ya Qrupu Bloklayar.
║
║▻ 🔮 Istifadə: /unblock
║▻ 📃 Açıqlama: Bloku Açar.
║
║▻ 🔮 Istifadə: /blocklist
║▻ 📃 Açıqlama: Blok olunanların siyahısını göstərər.
║
║▻ 🔮 Istifadə: /broadcastall
║▻ 📃 Açıqlama: Qrupa Və Şəxsiyə Yayım Edər.
║
║▻ 🔮 Istifadə: /gcast
║▻ 📃 Açıqlama: Qruplarda yayım edər.
║
║▻ 🔮 Istifadə: /broadcast_pin
║▻ 📃 Açıqlama: Qruplarda yayım edər və pinləyər.
║
║▻ 🔮 Istifadə: /dyno
║▻ 📃 Açıqlama: Heroku Dyno Miqdarını Ölçər.
║
║▻ 🔮 Istifadə: /pin
║▻ 📃 Açıqlama:  Yanıtlanan Mesajı Pinləyər.
╚═════════════════
"""

##### Broadcast Mesajları


class LAN(object):


    BILDIRIM = """**🆕 Yeni istifadəçi bota start etdi**\n\n👤 {}\n🆔 `{}`\n🔗 [{}](tg://user?id={})"""
    GRUP_BILDIRIM = """**🆕 Yeni istifdəçi bota qrupda start etdi**\n\n👤 Qrupa əlavə edən: `{}`\n🆔 Qrupa əlavə edən istifadəçi id: `{}`\n🔗 Profil linki: [{}](tg://user?id={})\nQrupun ID: {})

"""
    SAHIBIME = """
sahibimə
"""
    PRIVATE_BAN = """
Məyusam, əngəlləndiniz! Bunun bir xəta olduğunu düşünürsünüzsə {} yazın.
 """
    GROUP_BAN = """
Məyusam, qrupunuz qara siyahıya əlavə olundu! Artıq burada qala bilmərəm! Bunun bir xəta olduğunu düşünürsünüzsə {} yazın.'
"""
    NOT_ONLINE = """
aktiv deyil
"""
    BOT_BLOCKED = """
botu əngəlləyib
"""
    USER_ID_FALSE = """
istifadəçi ID yanlışdır.
"""
    BROADCAST_STARTED = """
```📥 Reklam yayımı başladı!\nBitəndə mesaj göndərəcəm
"""
    BROADCAST_STOPPED = """
```✅ Reklam yayımı uğurla tamamlandı.```\n\n**Bu qədər vaxtda tamamlandı** `{}`\n\n**Ümumi istifadəçilər:** `{}`\n\n**Ümumi göndərmə cəhdləri:** `{}`\n\n**Uğurla göndərilən:** `{}`\n\n**Ümumi xəta:** `{}`
"""
    STATS_STARTED = """
{} **Zəhmət olmasa gözləyin, bilgiləri gətirirəm!**
"""
    STATS = """
**@{} Məlumatları**\n\n**İstifadəçiləri;**\n» Ümumi: `{}`\n» Qruplar: `{}`\n» Şəxsi: `{}`\n\n**Disk İstifadəsi;**\n» Disk'in Sahəsi: `{}`\n» İstifadə Edilən: `{} ({}%)`\n» Boş Qalan: `{}`\n\n**🎛 Ən yüksək istifadə dəyərləri;**\n» CPU: `{}%`\n» RAM: `{}%`\n» Pyrogram: {}
"""
    BAN_REASON = """
Bu səbəbdən qadağan olundunuz @{} tərəfindən avtomatik olaraq yaradılmışdır."""
    NEED_USER = """
**Zəhmət olmasa istifadəçi ID'si yazın.**
"""
    BANNED_GROUP = """
🚷 **Qadağan olundu!\n\nQadağan edən:** {}\n**Qrup ID:** `{}`\n**Vaxt:** `{}`\n**Səbəb:** `{}`
"""
    AFTER_BAN_GROUP = """
**Məyusam, qrupunuz qara siyahıya əlavə edildi!\n\nSəbəb:** `{}`\n\n**Artıq burada qala bilmərəm. Bunun bir xəta olduğunu düşünürsünüzsə, dəstək qrupuna gəlin.**
"""
    GROUP_BILGILENDIRILDI = """\n\n✅ **Qrupu bilgiləndirdim və qrupdan çıxdım.**
"""
    GRUP_BILGILENDIRILEMEDI = """\n\n❌ **Qrupu məlumatlandırarkən xəta yarandı:**\n\n`{}`
"""
    USER_BANNED = """
🚷 **Qadağan olundu\n\nQadağan edən:** {}\n **İstifadəçi ID:** `{}`\n**Vaxt:** `{}`\n**Səbəb:** `{}`
"""
    AFTER_BAN_USER = """
**Məyusam, qara siyahıya əlavə edildiniz! \n\nSəbəb:** `{}`\n\n**Bundan sonra sizə xidmət etməyəcəyəm.**
"""
    KULLANICI_BILGILENDIRME = """\n\n✅ İstifadəçini məlumatlandırdım.
"""
    KULLANICI_BILGILENDIRMEME = """\n\n❌ **İstifadəçini məlumatlandırarkən xəta yarandı:**\n\n`{}`
"""
    UNBANNED_USER = """
🆓 **İstifadəçinin qadağası qaldırıldı!** \nQadağanı qaldıran: {}\n**İstifadəçi ID:** `{}`
"""
    USER_UNBAN_NOTIFY = """
🎊 Sizə gözəl bir xəbərim var! Artıq əngəliniz qaldırıldı!
"""
    BLOCKS = """
🆔 **İstifadəçi ID:** `{}`\n⏱ **Vaxt:** `{}`\n🗓 **Qadağan edildiyi tarix:** `{}`\n💬 **Səbəb:** `{}`\n\n"""
    TOTAL_BLOCK = """
🚷 **Ümumi əngəllənən:** `{}`\n\n{}
"""
