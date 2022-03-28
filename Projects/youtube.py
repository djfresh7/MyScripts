from pytube import YouTube
import os

# function to download YouTue videos
def download_yt_vid_file(videourl, path):
  yt = YouTube(videourl)
  yt = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
  if not os.path.exists(path):
    os.makedirs(path)
  yt.download(path)

download_yt_vid_file("https://www.youtube.com/watch?v=duLKCOmxbJs", "files/")

# function to download a youtube video's audio
ytvid = YouTube("https://www.youtube.com/watch?v=duLKCOmxbJs")
ytvid = ytvid.streams.first()
ytvidfile = ytvid.download("files/")

e = ytvidfile
print(e)