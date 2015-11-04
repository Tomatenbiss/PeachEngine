#Downloader for PeachEngine-Crawler

class Downloader:

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return 'Downloading: ' + self.url
