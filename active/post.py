from pyrogram import Client,filters
import httpx

@Client.on_message(filters.command("post"))
async def post(bot,msg):
  umi = "https://animepahe.ru/"
  query = msg.text.split(" ",1)[1]
  search_url = umi + "api?m=search&q=" + query
  response = httpx.get(search_url)
  amir = response.text
  f = open("new.txt", "w")
  f.write(amir)
  f.close()
  await msg.reply_document("new.txt")
  
  
  
