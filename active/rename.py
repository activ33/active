

import time, os
from pyrogram import Client, filters, enums
from File.utils import progress_message, humanbytes

@Client.on_message(filters.command("rename"))
async def rename(bot,msg):
  if len(msg.text) <= 7:
    return await msg.reply_text("Please Type New name with /rename command.",quote=True)
  reply = msg.reply_to_message
  new_name = msg.text.split(" ",1)[1]
  if reply != None:
    sts = await reply.reply_text("Processing...", quote=True)
    c_time = time.time()
    await bot.download_media(reply,file_name=new_name,progress=progress_message, progress_args=("Uploade Started.....", sts, c_time))
    path = f"downloads/{new_name}"
    await reply.reply_document(document=path,thumb="thumb.jpg",force_document=True,progress=progress_message, progress_args=("Uploade Started.....", sts, c_time))
    await sts.delete()
    os.remove(path)
  else:
    await msg.reply_text("Please Reply to a Document to Rename",quote=True)
    


