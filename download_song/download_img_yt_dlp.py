import yt_dlp
import os

def download_img_yt_dlp(youtube_url, output_folder="assets/img"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    options = {
        'writethumbnail': True,
        'skip_download': True,
        'outtmpl': f"{output_folder}/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([youtube_url])

