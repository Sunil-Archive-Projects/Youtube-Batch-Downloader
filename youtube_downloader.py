#python3
import logging
import youtube_dl
import sys
from pushbullet import Pushbullet

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#get the Pushbullet authorization key from the file in different directory
pushbullet_auth_filepath="./pushbullet_authkey.txt"

#read the Pushbullet auth code and Initiate it
with open(pushbullet_auth_filepath) as f:
	authkey=f.readline()
	pb = Pushbullet(authkey.strip())

#options to be sent for the YoutubeDL object
options={
			'outtmpl': './Videos/%(title)s_BY_%(uploader)s.%(ext)s',
			'forcefilename':'True',
			'download_archive':'./youtubeDL_archiveFile.txt',
			'format':'[height<=720]'#'bestvideo'			
	    }

#initiate the YoutubeDL object
ydl=youtube_dl.YoutubeDL(options)

#download the videos by acccessing the links from the text file
with open("./youtube_links.txt") as f:
	for link in f:
		#add link HEAD checking and regex to check validity of the URL
		try:
			result=ydl.extract_info(link)
		except Exception as e:
			#push = pb.push_note("ERROR Youtube-DL Script", str(e))
			#sys.exit(0)
			print("Error :"+e)

push = pb.push_note("Youtube-DL Script", "Success!!")