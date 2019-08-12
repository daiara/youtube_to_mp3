import csv, sys, os, shutil, youtube_dl, time
from time import sleep

#This is the introduction to the program and a bit of how to.
lines = ["Welcome to your very own downloading mp3 from YouTube system :)",
        "\nI'll ask you a few simple questions so you can use this without the supervision of an adult",
        "\nDo you want to download ONE song from one link or do you want to download several from a csv file?"]

#This block of code will make the text above appear to be typed in. It's just fun, you can delete it, change lines to print and the [] for ().
for line in lines:
    for c in line:
        print(c, end='')    
        sys.stdout.flush()  
        sleep(0.05)          
    print('')

def yt_dl(file_name, link, PATH): 
    if not os.path.exists(PATH + '/' + file_name + 'mp3'):
        print("\nDownloading: " + file_name)
        ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': file_name, 
                    'noplaylist': True, #If you want to download a playlist from youtube, check the * at the bottom
                    'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3', 
                    'preferredquality': '320',}],
                    }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            if PATH != '.':
                shutil.move((file_name + 'mp3'), PATH)

    else:
        print("\nThe song '" + file_name + "mp3' already exists.") #So you don't donwload the same song twice.


def folder_path():
    #Where will the songs be saved. It will create a folder with that name if you don't have it already.
    folder = input("\nWhere would you like it saved?\nGive me a path to a folder, please:\n>")
    
    if folder == '':
        folder = '.' #This will allowed for the download to be saved in the same folder as the py file.
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

#Choose a link or the csv
choice = input("\nType ONE to give me a link or CSV to give me a path to a csv with a playlist:\n>").upper()
if choice.startswith('O'):
    link = input("\nCopy/paste your link here:\n>") #Copy paste a youtube link
    file_name = input("What name would you like it saved with?\n>") + '.' #Same
    PATH = folder_path()
    yt_dl(file_name, link, PATH)

elif choice.startswith('C'):
    #This will only work if you use the sample csv.**
    #If you want to use just the song title, just delete the row["Artist"] + "-" + part from line 69.
    csv_file = input("\nWhat's the path to your csv with the links:\n>") 
    while not os.path.exists(csv_file):
        csv_file = input("Please check if the path is correct and try again:\n>")
    
    PATH = folder_path()
    with open(csv_file) as csv_data:
        reader = csv.DictReader(csv_data, delimiter=',')
        
        for row in reader:
            file_name = row["Artist"] + " - " + row['Title'] + '.' #This dot at the end is the one between song and mp3. Don't delete it by accident.
            link = row["Link"]
            yt_dl(file_name, link, PATH)
    
            
print("\nAnd that was it. Enjoy! :)")

"""
* If you want to download a playlist from youtube, make this changes from line 17 to line 36:
def yt_dl(link):
    ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 
                'preferredquality': '320',}],
                }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    
This will allow you to download a public playlist but you can't save the songs with the name you like or tranfer the songs
to a picked folder. The songs will be saved in the same folder where the py file is, and it will re-download songs that have
the same name. In this case, the csv is better.
**I added a sample of the csv file, just delete my links and add your own with the name of the song and artist. 
I personally prefer to use the csv mode because I can choose the file name this way and save the files on a different folder.
"""
