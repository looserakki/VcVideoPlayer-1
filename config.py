import os

from os import getenv

admins = {}
ADMIN = int(os.getenv('ADMIN',1956381927))
CHANNEL = int(os.getenv('CHANNEL',-1001173097859))
API_ID = int(os.getenv("API_ID", "8636372"))
API_HASH = os.getenv("API_HASH", "7dd38153ba6f48bfd990a8067e5b8498")
BOT_USERNAME = os.getenv("BOT_USERNAME", "VcVideoRobot")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Vc Video Player")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "DeeCodeSupport")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "DeeCodeBots")
SOURCE_CODE = os.getenv("SOURCE_CODE", "github.com/Sammy-XD/VcVideoPlayer")
BOT_TOKEN = os.getenv("BOT_TOKEN", "1937087520:AAGPzDeqUUEgNDTpDoUL3Gv8aPtUkXLOZV8")
SESSION_NAME = os.getenv("SESSION_NAME", "AQAvHkUGAXH2whSr0XsnauzwB4jAXzf_1lZl7wijYYxEqgUQAg0JXUs-NfhADAHlfvpO72g-nSGrvu7DrZCNQOWWIWCNHOxvFprxYx_eFRMjA16_LD3ypPi0c5j1T3bHRi62DFQQe4LpvUMkutSy7jLhjiNw-4gTAhJLX4PIQ4cKquFyUkxT035k-dww7yLT69AB6KCbNkQTO66eYkvk7RGcrEWI7p0LBfD5yIeMAEyngEjUuVxc89HEis5sx5nuXH4_SHftzC4_naNDCkuopv_wWhovZmykRhYzI-dX9vjM52MD3WccOw2ANtfr89ASXXn2MrCsXNOLqkDAkaKVEPgrdN7njwA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2012882227").split()))
