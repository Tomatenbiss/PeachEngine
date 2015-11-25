class TermFreq:
    def __init__(self, docTitle, termFreq):
        self.docTitle = docTitle
        self.termFreq = termFreq

    def __str__(self):
        return self.toString()

    def toString(self):
        return ("(%s, %d)" % (self.docTitle, self.termFreq))
