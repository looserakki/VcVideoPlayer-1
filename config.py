import os

from os import getenv

admins = {}
ADMIN = int(os.getenv('ADMIN',1956381927))
CHANNEL = int(os.getenv('CHANNEL',-1001173097859))
API_ID = int(getenv("API_ID", "8636372"))
API_HASH = getenv("API_HASH", "7dd38153ba6f48bfd990a8067e5b8498")
BOT_TOKEN = getenv("BOT_TOKEN", "2020813025:AAHvDTniAFZSnL1VWM3Z58Jp8W7Q7JSHl6w")
SESSION_NAME = getenv("SESSION_NAME", "AQBWf9iB4u4wz_lYcJyNFX65xCwoC5r_n4hXgZjGWE0dF7edd1JNpawcVU1kOsX-P7w-T7edpTGBBvraZKY0zlbvuBOEC0oqVVa_TKWvn3z0W3Pk8Tfwrp3x0X3ILR1j4FC2ecyZfHvtVjfIvm24dmOL4vVkFUdgjQvWDxRMPHia0eiQbP-WHbYqmBy-HCFvlMLcDptkj1ZwlvwZ-9YCk7x-cvGCWPjsD-POSF2WXvM-YbAD9BN2inYQfWKrwDJg4csujX5eIzBnv0PA-XkTfdJiIhE5qD01NfqQ4ZkLob_paMLekdzPe7typI7wPjQo2bFv5z5bujem-KMKwHjzbtlFdN7njwA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AsmSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsmSafone")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MyVideoPlayer")
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "hello")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2007701745").split()))
