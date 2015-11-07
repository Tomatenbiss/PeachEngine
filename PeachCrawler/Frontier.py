#Frontier for PeachEngine-Crawlers

from Downloader import Downloader
from Parser import Parser
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


    def peaching(self):
        self.manageSeed()
        self.manageAutomode()
        self.formatResultAndPrint()

    # FSK 18
    def cutChildFromParent(self, familyTree):
        child = ''
        try:
            childHTML = re.search('d[0-9]*\.(html|htm)?', familyTree).group()
            child = re.search('d[0-9]*', childHTML).group()
        except AttributeError:
            print 'No child found in ', family
        return child


    # Method to downLoad and parse the given seeds.
    # Adding each element to proofed[]
    def manageSeed(self):
        for x in range(0, len(self.seed)):
            # Put seed-element x in proofed[]
            self.proofed.append(self.seed[x])
            # Download x seed-element html into 'parent'
            parent = self.downloader.download(self.seed[x])
            # Cut the name of x seed-element child into 'child'
            child = self.cutChildFromParent(self.seed[x])
            # Pars all children from 'parent' & put them with parent-name in grandChildren[]
            grandChildren = self.parser.parsSeed(parent, child);
            # Append all grandChildren with new parent to toProof[]
            if len(grandChildren) >= 1:
                for index in range(1, len(grandChildren)):
                    self.toProof.append(self.staticDocumentLocation + grandChildren[index])
            # Add grandChildren[] to model[]
            self.model.insert(0, grandChildren)

    # Method to download and parse all elements from toProof[]
    # while adding new elements to toProof[] if current proofed
    # element is not an element of proofed[].
    def manageAutomode(self):
        while self.toProof:
            # Get and delete the last element from toProof[]
            familyMember = self.toProof.pop()
            if familyMember not in self.proofed:
                # Put 'familyMember' in proofed[]
                self.proofed.append(familyMember)
                # Download 'familyMember' html into 'parent'
                parent = self.downloader.download(familyMember)
                # Cut the name of 'parent' child into 'child'
                child = self.cutChildFromParent(familyMember)
                # Pars all children from 'parent' & put them with parent-name in grandChildren[]
                grandChildren = self.parser.parsSeed(parent, child);
                # Append all grandChildren with new parent to toProof[]
                if grandChildren:
                    for index in range(1, len(grandChildren)):
                        self.toProof.append(self.staticDocumentLocation + grandChildren[index])
                # Add grandChildren[] to model[]
                self.model.insert(0, grandChildren)

    def formatResultAndPrint(self):
        liste = sorted(self.model)
        output = ''
        for i in range(0, len(liste)):
            for index in range(0, len(liste[i])):
                string = liste[i][index]
                if string.endswith('html'):
                    if index != len(liste[i]) - 1 :
                        string = re.search('d[0-9]*', string).group() + ','
                    else:
                        string = re.search('d[0-9]*', string).group()
                output = output + string
            output = output + '\n'
        sys.stdout.write(output) 

        # for list in liste:
        #     output = output + '\n'
        #     for number in list:
        #         if number.endswith('html'):
        #             number = re.search('d[0-9]*', number).group()
        #         output = output + ',' + number
        # print'output:\n', output
