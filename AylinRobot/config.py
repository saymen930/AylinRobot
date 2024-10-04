# 
# 
# 
# 

# 
# 
# 

import os

class Config:

   API_ID = int(os.getenv("API_ID", "16501912"))
   API_HASH = os.getenv("API_HASH", "34138f0596a914d229f8bc1ab7794bc6")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6999080991:AAFm-Sad9EBJuGYA_y8BWLKNyHSMtBmgLeA")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "EsilaChatBot")
   BOT_NAME = os.environ.get("BOT_NAME", "Esila Sohbet")   
   OWNER_ID = int(os.environ.get("OWNER_ID","6153472412"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "debubluman") 
   GONDERME_TURU = bool(os.environ.get("GONDERME_TURU", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://emir:emir@cluster0.c2npk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002036606687"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "esilabotbilgilendirme")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002022150339"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002036606687"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "HRKU-dde44331-5d75-4c7f-8437-c774c4e5503a")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Emir")
   CHANNEL = os.environ.get("CHANNEL", "esilabotbilgilendirme")
   SUPPORT = os.environ.get("SUPPORT", "sorundestekk")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://envs.sh/SGJ.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
