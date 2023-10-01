

from pyrogram import Client,filters,enums
import os,time
from File.utils import progress_message, humanbytes

@Client.on_message(filters.command("batch"))
async def batch(bot,msg):
  reply = msg.reply_to_message
  text = msg.text.split(" ",1)[1]
  if '#zzz' in text:
    file = text.split("#zzz",1)
    numb = file[0]
    fname = file[1]
    j = int(numb)
  else:
    return await bot.send_message(msg.chat.id,"Please add #zzz & number in text")
  start = reply.id-1
  end = msg.id+1
  for i in range(start,end):
       c = await bot.get_messages(msg.chat.id,i)
       cd = c.media
       if i==start:
         await bot.send_message(msg.chat.id,"Renaming Started...")
       elif cd != None:
         sts = await c.reply_text(f"Document - {j} Downloading Started")
         c_time = time.time()
         full_name = f"{j} - {fname}"
         down = await bot.download_media(c,file_name=full_name,progress=progress_message, progress_args=("Download Started.....", sts, c_time))
         up = await bot.send_document(msg.chat.id,document=f"downloads/{full_name}",thumb="thumb.jpg",progress=progress_message, progress_args=("Uploade Started.....", sts, c_time))
         path = f"downloads/{full_name}"
         os.remove(path)
         j = j+1
         await sts.delete()
         
        
    