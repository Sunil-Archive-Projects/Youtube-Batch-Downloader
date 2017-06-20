Features:
- Download hundreds of videos on one run. No more tubemating videos one by one
- Keep it for downloading, take a walk. When it is done, it'll send notification to your Mobile through pushbullet integration
- Configurable Video Quality 
- Ability to download Music only if needed



How to run the Youtube Downloader :


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


Future Enhancements :

Read the youtube_links.txt from a remote file. Run the script from RaspberryPi periodically using CRON job to have media center of offline streamable high quality videos.


