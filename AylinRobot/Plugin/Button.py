from AylinRobot.config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
  
### START BUTTONU 

START_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('📢 Kanal', url=f"https://t.me/{Config.CHANNEL}"),
InlineKeyboardButton("💬 Sohbet Qrupu", url=f"https://t.me/{Config.SUPPORT}"),
],[
InlineKeyboardButton('ℹ️ Bot Hakkında', callback_data='bh'),  
InlineKeyboardButton('📚 Bot Komutları', callback_data='help'),
],[        
InlineKeyboardButton('➕ Beni grupuna ekle ➕', url=f"https://t.me/{Config.BOT_USERNAME}?startgroup=true"),
],[                
InlineKeyboardButton('👨🏻‍💻 Bot Sahibi',  url=f"https://t.me/{Config.OWNER_NAME}"),
InlineKeyboardButton('🎧 Playlist', url=f"https://t.me/{Config.PLAYLIST_NAME}"),]])

#### KÖMƏK BUTTONU

HELP_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🎧 Şarkı', callback_data='musıc'),
InlineKeyboardButton('⭐ Telegraph', callback_data='tg')
],[
InlineKeyboardButton('🎲 Oyunlar', callback_data='oyun'),
InlineKeyboardButton('🇦🇿 Şehitler', callback_data='sehıd'),
],[        
InlineKeyboardButton('🌀 Eğlence', callback_data='eylence'),
InlineKeyboardButton('♾️ extra', callback_data='elave'),
],[
InlineKeyboardButton('🔍 Arama', callback_data='axtar'),
InlineKeyboardButton('🔔 Etiket', callback_data='tag'),    
],[
InlineKeyboardButton('👨🏻‍💻 Sahib Komutları', callback_data='sahib'),
],[    
InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='home'),]])

### GERİ BUTTONU    

MUSIC_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='help'),]])
TELEGRAPH_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='help'),]])
SEHID_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='help'),]])        
OYUN_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='help'),]])
EYLENCE_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='help'),]])     
SAHIB_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='help'),]])
ELAVE_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='help'),]])
AXTAR_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='help'),]])
TAGGER_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='help'),]])
BH_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('✖️ Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri Dön', callback_data='home'),]])
