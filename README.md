# YouTube -> PeerTube
This script is written in Python3, that download (videos/playlists) from YouTube channels and upload to PeerTube channels.

## Installation
To install, clone the repository to a directory on your machine. Then, navigate to that directory in a terminal and run: 
```bash
git clone https://github.com/ivansaul/YouTube-PeerTube.git
```
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
This will create a virtual environment for the tool and install all dependencies required to run.

## Configuration
An example configuration file is found at `config_example.toml`. Copy this and rename to `config.toml` and replace the fields with your information

These are configuration fields.
- `peertube_instance` : URL of peertube instance.
- `peertube_channel` : Peertube channel handle to upload video.
- `peertube_username` : Peertube username.
- `peertube_password` : Peertube password WARNING this file needs to be secure.
- `peertube_channel_category` : Category of channel contents (music, films, vehicles, sport, travels, gaming, people, comedy, entertainment, news, how to, education, science & technology, animals).
- `default_lang` : Default channel language (english, french, german, italian, japanese, korean, mandarin, portuguese, russian, spanish).
- `delete_videos` : Delete videos and metadata after upload to peertube (True, False).
- `privacy_videos` : Privacy for entire upload videos (public, private, unlisted).

## Running the script
- If you want to download a `list of YouTube videos` and then upload them to PeerTube.
     1. Open `videos.txt` and paste the urls of the YouTube videos you want to upload to PeeTube.
     2. Run `videos.py`.
     3. The script will ask you for the name of the playlist where you want the videos to be saved.

- If you want to download a `list of YouTube PlayLists` and then upload them PeerTube.
     1. Open `playlist.txt` and paste the urls of the YouTube playlists you want to upload to PeeTube.
     2. Run `playlist.py`.