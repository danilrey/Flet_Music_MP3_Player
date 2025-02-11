import yt_dlp
import os
from .download_img_yt_dlp import download_img_yt_dlp as youtube_dl_img

def download_audio_yt_dlp(youtube_url, output_folder="downloads"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f"{output_folder}/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([youtube_url])

    youtube_dl_img(youtube_url)

