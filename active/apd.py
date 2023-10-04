import tqdm
import os
from kwik_token import get_dl_link
import pahe  # Import animepahe module
from colorama import Fore
from pyrogram import Client,filters

# Function to replace special characters in a string
def replace_special_characters(input_string, replacement="_"):
    special_characters = "!@#$%^&*()_+{}[]|\\:;<>,.?/~`"
    for char in special_characters:
        input_string = input_string.replace(char, replacement)
    return input_string

@Client.on_message(filters.command("pahe"))
async def nonee(bot,msg):
  hero = msg.text.split(",")
  query = hero[1]
  choice = int(hero[2])
  episode_range = hero[3].split("-")
  lang = "jpn"
  quality = int(hero[4])
  list_of_anime = pahe.search_apahe(query)
  anime_id = list_of_anime[choice][6]
  episode_range = (
    [int(episode_range[0]), int(episode_range[1]) + 1]
    if len(episode_range) == 2
    else [int(episode_range[0]), int(episode_range[0]) + 1]
)
  episode_ids = pahe.mid_apahe(session_id=anime_id, episode_range=episode_range)
  episodes_data = pahe.dl_apahe1(anime_id=anime_id, episode_ids=episode_ids)
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
  for key, items in episodes.items():
    backup_quality = list(episodes[key][lang])[-1]
    try:
       episodes[key] = episodes[key][lang][quality][0]
    except:
      try:
         episodes[key] = episodes[key][lang][backup_quality][0]
      except:
       pass
  for key, value in tqdm.tqdm(episodes.items(), desc="Parsing links"):
    episodes[key] = pahe.dl_apahe2(value)
    print(episodes[key])
  title = replace_special_characters(list_of_anime[choice][0])
  if not os.path.exists("Anime"):
     os.makedirs("Anime")
  for key, value in tqdm.tqdm(episodes.items(), desc="Downloading Episodes"):
    destination = os.path.join("Anime",f"{key} - {title} [{quality}p] [ESH] @AnimeFiles.mkv")
    download_link = get_dl_link(value)
    print("download_link")
    sts = await msg.reply("Downloading Started")
    anime = pahe.download_file(url=download_link, destination=destination)
    upl = await msg.reply_document(document=destination)
    os.remove(destination)
    await sts.delete()
