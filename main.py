from pytube import YouTube
from pytube.cli import on_progress

try:
    #Enter video link
    link = input("Enter the link: ") 
    yt = YouTube(link, on_progress_callback = on_progress)
    
    #Details of the video
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length,"seconds")

    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

except:
    #Raise error if invalid link entered
    print("Invalid URL")

#Downloading the video
try:
    print("\nProgress: ")
    ys.download("YOUR_PATH")
    print("\nSuccessfully Downloaded...")
except: 
    print("\nCouldn't download video")
    
