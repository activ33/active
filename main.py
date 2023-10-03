from os import environ
from pyrogram import Client

plugins = dict(root="active")
api = 24541704
hash = "7b1b63a5c5a2e53233a0e78727c068d3"
token = environ.get("token")

print("⚡ Starting...")
Client("Active", api_id=api, api_hash=hash, bot_token=token,
       plugins=plugins).run()
