#python3
import youtube_dl
import sys
from pushbullet import Pushbullet

#get the Pushbullet authorization key from the file in different directory
pushbullet_auth_filepath="C:\Temp\Python_auth\pusbullet_authkey.txt"

#read the Pushbullet auth code and Initiate it
with open(pushbullet_auth_filepath) as f:
	authkey=f.readline()
	pb = Pushbullet(authkey.strip())

#options to be sent for the YoutubeDL object
options={
			'outtmpl': 'C:/Temp/Youtube/audios/%(title)s_BY_%(uploader)s.%(ext)s',
			
			#'verbose':'True',
			#'forcedescription':'True',
			#'playliststart':96,
			#'writethumbnail':'True',
			#'writeinfojson':'True',
			#'listformats':'True',
			'noplaylist':'True',
			'forcefilename':'True',
			'download_archive':'C:\Temp\Python_auth\youtubeDL_audioarchiveFile.txt',
			'format': '141/140'
	    }

#initiate the YoutubeDL object
ydl=youtube_dl.YoutubeDL(options)

#download the videos by acccessing the links from the text file
with open("C:/Temp/Python_auth/youtube_links.txt") as f:
	for link in f:
		#add link HEAD checking and regex to check validity of the URL
		try:
			result=ydl.extract_info(link)
		except Exception as e:
			push = pb.push_note("ERROR Youtube-DL Script", str(e))
			sys.exit(0)

push = pb.push_note("Youtube-DL Script", "Success downloading audio!!")