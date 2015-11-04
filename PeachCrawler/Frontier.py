#Frontier for PeachEngine-Crawlers

from Downloader import Downloader
#from Parser import Parser

class Frontier:

    def __init__(self, seed):
        self.seed = seed
        self.toProof = []
        self.proofed = []

    def peaching(self):
        print 'peaching...'
        self.parsSeed()
        #startAuto()

    # Method to downLoad and parse the given seed
    def parsSeed(self):
        downloader = Downloader()
        for x in range(0, len(self.seed)):
            self.proofed.insert(0, self.seed[x])
            string = downloader.download(self.seed[x])
            print(string)
        print(self.proofed)

    # Method to download and parse A given webLink
    def parsURL(self, webLink):
        pass

    # Method to call passURL until all destinations are proofed
    def startAuto(self):
        pass
