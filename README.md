Features:






How to run the Downloader :


1. Make sure that Python 3.x is installed from https://www.python.org/downloads/

2. Clone or Download the project to local system

3. Run the following command in the directory in which script is downloaded:
	
		pip install --upgrade --force-reinstall -r requirements.txt

	This will ensure you have latest version of youtube-dl. Youtube keeps on changing the way it processes the videos, so it is best to upgrade it once every week

4. Run youtube_downloader.py with the following command in cmd or bash:
		
		-- For videos
		python youtube_downloader.py 

		--For audio only
		python youtube_downloader_audioOnly.py

	Make sure that following files are already present in the same directory:

		- youtube_links.txt
			- This contains all the links from youtube which you want to download
			- Each link can be of a individual video or a playlist. If it is a playlist, then it'll download all the videos in that playlist

		- pushbullet_authkey.txt
			- Contains access token through which the script can send appropriate Pushbullet notifications
			- Get pushbullet access token at https://www.pushbullet.com/#settings/account


