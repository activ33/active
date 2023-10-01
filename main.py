from pyrogram import Client

plugins = dict(root="active")
api = 3459865
hash = "815c6badc99076374aee0e11c1305edd"
token = "6661866494:AAEmoQ34gldBa5hxsOipqJIU2GD1c3OS8zs"

print("⚡ Starting...")
Client("Active", api_id=api, api_hash=hash, bot_token=token,
       plugins=plugins).run()
