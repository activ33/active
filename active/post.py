from pyrogram import Client,filters

@Client.on_message(filters.command("post"))
async def post(bot,msg):
  await msg.reply_document("new.txt")
                     
  
  
  
