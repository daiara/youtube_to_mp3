## Youtube to MP3

This program allows you to download songs from youtube as mp3 files, from a link or a csv file.

First of all, you need to be using Python 3. 

Second of all, you need the youtube_dl library 

Use ```pip install youtube-dl``` to download it to your computer.

This was made and tested on a Mac osx. I tested on a linux and it had issues.

Check the ```yt_sample.csv``` for how to save a youtube playlist with the titles that you like. 

A few modifications on the code are allowed as the comments below show.

If you want to download a playlist from youtube, make this changes from line 17 to line 36: 
```
def yt_dl(link): 
  ydl_opts = { 
    'format': 'bestaudio/best', 
    'postprocessors': [{ 
    'key': 'FFmpegExtractAudio', 
    'preferredcodec': 'mp3', 
    'preferredquality': '320',}], }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
    ydl.download([link])
```
This will allow you to download a public playlist but you can't save the songs with the name you like or tranfer the songs to a picked folder. The songs will be saved in the same folder where the py file is, and it will re-download songs that have the same name and that's why I think the csv is better.

I added a sample of the csv file, just delete my links and add your own with the name of the song and artist. I personally prefer to use the csv mode because I can choose the file name this way and save the files on a different folder.
