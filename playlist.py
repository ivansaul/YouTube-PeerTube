#!/usr/bin/env python
# coding: utf-8

# ## **Modules**

# In[11]:


import os
import re
import toml
import pandas as pd
from sty import fg, rs
from pytube import YouTube
from pytube import extract
from pytube import Playlist


# ## **PeerTube secrets**

# In[12]:


config = toml.load("config.toml")

username = config['peertube_username']
password = config['peertube_password']
instance = config['peertube_instance']
channel = config['peertube_channel']
category = config['peertube_channel_category']
language = config['default_lang']
delete_videos = config['delete_videos'].lower() in ['true','yes']
privacy = config['privacy_videos']


# ### Make PeerTube secrets for `prismedia`

# In[13]:


import requests
response = requests.get(f'{instance}/api/v1/oauth-clients/local')
secrets = response.json() #print(secrets)

#write secrets file
f = open("peertube_secret", "w")
f.write("[peertube]\n")
f.write(f"client_id = {secrets['client_id']}\n")
f.write(f"client_secret = {secrets['client_secret']}\n")
f.write(f"username = {username}\n")
f.write(f"password = {password}\n")
f.write(f"peertube_url = {instance}\n")
f.write("OAUTHLIB_INSECURE_TRANSPORT = '0'")
f.close()


# ## **Functions**

# In[14]:


def down(url, output_path):
    yt = YouTube(url)
    title=yt.title
    title=re.sub(r"[^a-zA-Z0-9]+", ' ', title)
    video=yt.streams.get_highest_resolution()
    video.download(output_path= output_path, filename=title)

def upl(file_path, url, channel, play_list, category, language, privacy):
    yt = YouTube(url)
    title=yt.title
    title=re.sub(r"[^a-zA-Z0-9]+", ' ', title)
    os.system(f'prismedia --file="{file_path}/{title}.mp4" --platform=peertube --privacy="{privacy}" --category="{category}" --language="{language}" --channel="{channel}" --playlist="{play_list}" --channelCreate --playlistCreate')

def get_id(url):
    return extract.video_id(url)

def del_folder(path_folder):
    import shutil
    shutil.rmtree(path_folder)


# ## **===============================**

# ## **Playlist folder / files**

# In[15]:


with open('playlist.txt') as f:
    urls_pl = f.readlines()
    
urls_pl = [x.strip() for x in urls_pl]
urls_pl = list(filter(None, urls_pl))

for url_pl in urls_pl:
    #playlist object
    pl = Playlist(url_pl)
    #playlist name 
    play_list=pl.title #play_list='rock'
    
    output_path = f'data/{channel}/{play_list}'
    csv_file = f'data/{channel}/{play_list}.csv'
    
    #make folder
    import errno
    try:
        os.makedirs(f'data/{channel}/{play_list}')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
    #verify if csv file exist or not
    if not os.path.isfile(csv_file):
        # Create DataFrame 
        df = pd.DataFrame({'id':[]})
        df.to_csv(csv_file, index=False)


# ## **Download video from YouTube**

# In[ ]:


j,m=1,len(urls_pl)
for url_pl in urls_pl:
    pl = Playlist(url_pl)
    #playlist name 
    play_list=pl.title #play_list='rock'
    
    urls=pl.video_urls
    i,n=1,len(urls)
    for url in urls:
        print(fg.blue + f'[{j} / {m}][{i} - {n}]' + fg.rs)
        try:
            yt_id=get_id(url)
            df=pd.read_csv(csv_file)
        
            if yt_id in df['id'].values:
                print(fg.yellow + f'{yt_id} : This video was previously uploaded' + fg.rs)
            else:
                try:
                    #download / upload video
                    down(url,output_path)
                    print(fg.green + f'{yt_id} : Video Downloaded Successfully' + fg.rs)
                    upl(output_path, url, channel, play_list, category, language, privacy)
                    #update csv
                    df = df.append({'id':yt_id}, ignore_index=True)
                    df.to_csv(csv_file, index=False)        
                    print(fg.green + f'{yt_id} : Video Uploaded Successfully' + fg.rs)
                except Exception as e:
                    print(fg.red + f'Some unexpected error occurred : https://youtu.be/{yt_id}' + fg.rs)
                    print(fg.red + str(e) +fg.rs)
        except Exception as e:
            print(fg.red + f'ERROR! this url is probably wrong: {url}' + fg.rs)
            print(fg.red + str(e) +fg.rs)
        print(' ')
        i=i+1
    j=j+1


# ## **Delete download video folder**

# In[ ]:


for url_pl in urls_pl:
    #playlist object
    pl = Playlist(url_pl)
    #playlist name 
    play_list=pl.title #play_list='rock'
    
    output_path = f'data/{channel}/{play_list}'

    if delete_videos:
        del_folder(output_path)
        print(f'🗑️ All videos on the {play_list} playlist were removed')

