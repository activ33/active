import grequests
import requests
import re
import json
from tqdm import tqdm
from pyrogram import Client,filters
session=requests.session()
api = 24541704
hash = "7b1b63a5c5a2e53233a0e78727c068d3"
token = "6404643240:AAHXGBSIxyOFuHu2H9zBg0RqhcO05xQyApg"


app = Client("app",api_id=api,api_hash=hash,bot_token=token)

# Base URL for animepahe.ru
url = "https://animepahe.ru/"

# Search Apahe
@app.on_message(filters.command("pahe"))
async def pahe(bot,msg):
  query = msg.text.split(" ",1)[1]
  global url
  search_url = url + "api?m=search&q=" + query
  response = session.get(search_url)
  msg.reply(response.text.split(",",1)[0])

app.run()
  
