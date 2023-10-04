from pyrogram import Client,filters
from requests_html import HTMLSession
s = HTMLSession()

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

@Client.on_message(filters.command("hero")
async def hero(bot,msg):
  await msg.reply_document("new.txt")
                     
  
  
  
