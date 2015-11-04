#Downloader for PeachEngine-Crawler
from urllib2 import urlopen
import traceback

class Downloader:

    def __init__(self):
        self.url = "url"

    def __str__(self):
        return 'Downloading: ' + self.url

    def download(self, webLocation):
        html = ''
        try:
            url = urlopen(webLocation)
            html = url.read()
        except Exception, err:
            traceback.print_exc()
        return html
