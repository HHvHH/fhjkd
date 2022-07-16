import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "19351645"))
    API_HASH = os.environ.get("API_HASH", "359f66a067069b8b5c482df6a8a4e3b8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "o7Tbot")
    SUPPORT = os.environ.get("SUPPORT", "HASONI_LQ")
    CHANNEL = os.environ.get("CHANNEL", "HASONI_LQ")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/9157151068a4f3cae8445.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9157151068a4f3cae8445.jpg")
