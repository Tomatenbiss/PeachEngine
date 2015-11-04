#Downloader for PeachEngine-Crawler
from urllib2 import urlopen
import traceback

# Class definition of the class Downloader
# Provids an object to download a specific
# URL.
class Downloader:

    #Constructor
    def __init__(self):
        self.url = "url"

    #Std. method. Just for information purpose.
    def __str__(self):
        return 'Downloader of the PeachEngine-Crawler'

    # Method to download a given web-location.
    # Returns the context of the html document as string
    def download(self, webLocation):
        html = ''
        try:
            url = urlopen(webLocation)
            html = url.read()
        except Exception, err:
            traceback.print_exc()
        return html
