#Parser for PeachEngine-Crawler
from bs4 import BeautifulSoup
class Parser:


    def __str__(self):
        return 'Parser of the PeachEngine-Crawler'

    def parsSeed(self, URL, child):
        _grandchildren = [ ]
        _grandchildren.insert(0, child + ':')
        #_hrefs = [ ]
        _soup = BeautifulSoup(URL)
        for link in _soup.find_all('a'):
            _grandchildren.append(link.get('href'))
        #_grandchildren.append(_hrefs)
        return _grandchildren
 
