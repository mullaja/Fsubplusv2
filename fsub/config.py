import os

from dotenv import load_dotenv
from logging import basicConfig, INFO, WARNING, getLogger, Logger

load_dotenv("config.env", override=True)


BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_DB = int(os.getenv("CHANNEL_DB"))
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

RESTRICT = os.getenv("RESTRICT", True)

BUTTON_TITLE = os.getenv("BUTTON_TITLE", "Join")
BUTTON_ROW = int(os.getenv("BUTTON_ROW", 2))

FORCE_SUB_ = {}
FSUB_TOTAL = 1
while True:
    key = f"FORCE_SUB_{FSUB_TOTAL}"
    value = os.getenv(key)
    if value is None:
        break
    FORCE_SUB_[FSUB_TOTAL] = int(value)
    FSUB_TOTAL += 1

START_MESSAGE = os.getenv(
    "START_MESSAGE",
    "Halo {mention}!"
    "\n\n"
    "Saya dapat menyimpan file pribadi di Channel tertentu dan pengguna lain dapat mengaksesnya dari link khusus.",
)
FORCE_MESSAGE = os.getenv(
    "FORCE_MESSAGE",
    "Halo {mention}!"
    "\n\n"
    "Anda harus bergabung di Channel/Group terlebih dahulu untuk melihat file yang saya bagikan."
    "\n\n"
    "Silakan Join Ke Channel/Group terlebih dahulu.",
)

ADMINS = [int(x) for x in (os.getenv("ADMINS").split())]
    
CUSTOM_CAPTION = os.getenv("CUSTOM_CAPTION", None)
DISABLE_BUTTON = os.getenv("DISABLE_BUTTON", False)


basicConfig(level=INFO, format="[%(levelname)s] - %(message)s")
getLogger("hydrogram").setLevel(WARNING)
def LOGGER(name: str) -> Logger:
    return getLogger(name)