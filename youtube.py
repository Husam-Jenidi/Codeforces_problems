import pytube
url = "https://www.youtube.com/watch?v=KT44aQ_10XM&list=RDMM&index=10"
path="C:/Users/husam/Documents/Genova university/extra"
pytube.YouTube(url).streams.get_highest_resolution().download(path)
