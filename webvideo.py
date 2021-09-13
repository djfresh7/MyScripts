import requests
import time

# function to download web videos
def download_files(url, name):
  r = requests.get(url, stream=True)
  with open(name, "wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
      if chunk:
        f.write(chunk)

def get_video():
  download_files("https://www.youtube.com/watch?v=GeZvYukPDig", "smh.mp4")
  t = open("smh.mp4", "rb")
  print(t)