from pyrogram import Client

plugins = dict(root="active")
api = 24541704
hash = "7b1b63a5c5a2e53233a0e78727c068d3"
token = "6661866494:AAEmoQ34gldBa5hxsOipqJIU2GD1c3OS8zs"

print("⚡ Starting...")
Client("Active", api_id=api, api_hash=hash, bot_token=token,
       plugins=plugins).run()
