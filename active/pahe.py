



import grequests
import tqdm
import os,time
from active.kwik import get_dl_link
import active.utils as util
from colorama import Fore
from pyrogram import Client,filters
from active.prog import progress_message, humanbytes

# Replace Script
def replace_special_characters(input_string, replacement="_"):
  special_characters = "!@#$%^&*()_+{}[]|\\:;<>,.?/~`"
  for char in special_characters:
    input_string = input_string.replace(char, replacement)
  return input_string

@Client.on_message(filters.command("pahe"))
async def pahe(bot,m):
  lol = m.text.split(",")
  query = lol[1]
  choice = int(lol[2])
  rango = lol[3]
  episode_range = rango.split("-")
  n = await m.reply("processing...")
  list_of_anime = util.search_apahe(query)
  await n.edit_text(list_of_anime)
  anime_id = list_of_anime[choice][6]
  await n.edit_text(anime_id)
  episode_range = (
    [int(episode_range[0]), int(episode_range[1]) + 1]
    if len(episode_range) == 2
    else [int(episode_range[0]), int(episode_range[0]) + 1]
)
  await n.edit_text(episode_range)
  episode_ids = util.mid_apahe(session_id=anime_id, episode_range=episode_range)
  await n.edit_text(episode_ids)
  episodes_data = util.dl_apahe1(anime_id=anime_id, episode_ids=episode_ids)
  n.edit_text(episodes_data)
  episodes = {}
  index = episode_range[0]
  for key, value in episodes_data.items():
    sorted_links = {}
    for link_info in value:
      link, size, lang = link_info
      size = int(size.split('p')[0])
      if lang == '':
        lang = 'jpn'
      if lang not in sorted_links:
        sorted_links[lang] = {}
      if size not in sorted_links[lang]:
        sorted_links[lang][size] = []
      sorted_links[lang][size].append(link)
    episodes[index] = sorted_links
    index += 1
  await n.edit_text(episodes)
  lang = lol[4]
  quality = lol[5]
  for key, items in episodes.items():
    backup_quality = list(episodes[key][lang])[-1]
    try:
      episodes[key] = episodes[key][lang][backup_quality][0]
    except:
      pass
  for key, value in tqdm.tqdm(episodes.items(), desc="Parsing links"):
    episodes[key] = util.dl_apahe2(value)
    print(episodes[key])
  await n.edit_text(episodes[key])
  title = replace_special_characters(list_of_anime[choice][0])
  if not os.path.exists("Anime"):
    os.makedirs("Anime")
  for key, value in tqdm.tqdm(episodes.items(), desc="Downloading Episodes"):
    destination = os.path.join("Anime",f"{key} - {title} [{quality}p] @AnimeFiles.mkv")
    download_link = get_dl_link(value)
    print("download_link")
    util.download_file(url=download_link, destination=destination)
    sts = await m.reply("⚡ Processing...")
    c_time = time.time()
    upload = await m.reply_document(document=destination,progress=progress_message,thumb="Thumb.jpg", progress_args=("Uploade Started.....", sts, c_time))
    await sts.delete()
    os.remove(destination)
    
  
