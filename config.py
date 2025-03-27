import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 27173606
API_HASH = "cb98a9ce2fa3dd0ddd4906a3b71f0609"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7893951728:AAFhuA47sqiNw4tf4Tj7kQyZ9eX6pfuJEDc"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://JOHNWICK:JOHNWICK@cluster0.vpxt8ra.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = 6436590030

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6436590030

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/sukuna_pop2"
SUPPORT_GROUP = "https://t.me/sukuna_pop2"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQAf70YALzSu5189_pfxo1jT3sdLsxLjea_oyhms5pov1Kre0fdmjN5pHXAF7byUjhxmLN-wIWAdQzWyQQfjk9uYRQZw7PhSTkNZvpEX85geoVoqfMj5jjG7ZdgQd8LYhxJ3uQkFKWBwmdi7YDMp9yIs5ddL9XznpDKfEch4N5BAeEx42TsBpsD4k2FgAer5S_1sLQb1_8BgxYFepApRDbV5wNend06WG8e_SLQ3DN2Q4HqYBA3NbNz2wUHo1-AfflJ_9AiQcK6OEy1Sbi4UpJXNj0_Vc9vMU9uWO6bi5eF0O2w0pNcrqmCrt5TEvzORv10DYECErHsu1kT5sxLNVjxwh5bDgwAAAAHBhq7SAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"

PING_IMG_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"
STATS_IMG_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"
STREAM_IMG_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/c7dc1e8e9b3d57bf1cf61-e455a872526973229b.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
