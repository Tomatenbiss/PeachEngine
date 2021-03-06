#Frontier for PeachEngine-Crawlers

from PeachCrawler.Downloader import Downloader
from PeachCrawler.Parser import Parser
import re
import sys

class Frontier:

    def __init__(self, seed):
        self.staticDocumentLocation = 'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/'
        self.seed = seed
        self.toProof = []
        self.proofed = []
        self.model = []
        self.downloader = Downloader()
        self.parser = Parser()

    # Method to start the crawling
    # First the given seed, in addition all other linked pages
    def peaching(self):
        self.manageSeed()
        self.manageAutomode()

    # Method to get a sorted list of all crawled pages
    def pageLinks(self):
        return sorted(self.proofed)

    # FSK 18
    # Method to get the html document name of a full given link
    def cutChildFromParent(self, familyTree):
        child = ''
        try:
            childHTML = re.search('d[0-9]*\.(html|htm)?', familyTree).group()
            child = re.search('d[0-9]*', childHTML).group()
        except AttributeError:
            print ("No child found in", family )
        return child


    # Method to downLoad and parse the given seeds.
    # Marking each element as no canditate chain
    def manageSeed(self):
        for x in range(0, len(self.seed)):
            self.proofed.append(self.seed[x])
            parent = self.downloader.download(self.seed[x])
            child = self.cutChildFromParent(self.seed[x])
            grandChildren = self.parser.parsSeed(parent, child);
            if len(grandChildren) >= 1:
                for index in range(1, len(grandChildren)):
                    self.toProof.append(self.staticDocumentLocation + grandChildren[index])
            self.model.insert(0, grandChildren)

    # Method to download and parse all elements to proof
    # while adding new elements to, if current proofed
    # element is not a candidate chain.
    def manageAutomode(self):
        while self.toProof:
            familyMember = self.toProof.pop()
            if familyMember not in self.proofed:
                self.proofed.append(familyMember)
                parent = self.downloader.download(familyMember)
                child = self.cutChildFromParent(familyMember)
                grandChildren = self.parser.parsSeed(parent, child);
                if grandChildren:
                    for index in range(1, len(grandChildren)):
                        self.toProof.append(self.staticDocumentLocation + grandChildren[index])
                self.model.insert(0, grandChildren)


    # Method to generate a string representing the page structure
    def pageStructure(self):
        liste = sorted(self.model)
        output = ''
        try:
            for parentIndex in range(0, len(liste)):
                for childIndex in range(0, len(liste[parentIndex])):
                    string = liste[parentIndex][childIndex]
                    if string.endswith('html'):
                        if childIndex != len(liste[parentIndex]) - 1 :
                            string = re.search('d[0-9]*', string).group() + ','
                        else:
                            string = re.search('d[0-9]*', string).group()
                    output = output + string
                output = output + '\n'
        except AttributeError:
            sys.stderr.write('Error\n')
        return output

    # Method to generate a dictionary representing the page structure
    # Dictionary-Key = Parent as String
    # Dictionary-Value = Childs as List of Strings
    def pageStructureDic(self):
        string_list = self.pageStructure().split();
        # very bad hack sry
        empty = []
        lenght = len(string_list);
        link_graph = { }

        for x in range(0, lenght):
            mystring = string_list[x]
            key = mystring.split(":")
            values = key[1].split(",")
            if values[0] == '':
                tmp = { key[0]: empty}
            else:
                tmp = { key[0]: values}
            link_graph.update(tmp)
        return link_graph
