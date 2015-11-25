from TermFreqList import TermFreqList

class Token(object):
    def __init__(self, name, docTitle, value):
        self.name = name
        self.tf = TermFreqList(docTitle, value)

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return self.toString()

    def toString(self):
        res = ""
        return ("(%s, df:%d) -> [%s]" % (self.name, self.tf.len(), self.tf.toString()))

    def add(self, docTitle, value):
        self.tf.add(docTitle, value)
        
