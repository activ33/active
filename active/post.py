from pyrogram import Client,filters
import requests
from telegraph import Telegraph
from requests_html import HTMLSession
rqq = HTMLSession()
s = requests.Session()
telegraph = Telegraph()
telegraph.create_account(short_name='1337')

@Client.on_message(filters.command("post"))
async def post(bot,msg):
  umi = "https://animepahe.ru/"
  query = msg.text.split(" ",1)[1]
  search_url = umi + "api?m=search&q=" + query
  response = s.get(search_url)
  amir = response.text
  f = open("new.txt", "w")
  f.write(amir)
  f.close()
  await msg.reply_document("new.txt")
  
  
  
