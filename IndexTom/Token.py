from TermFreqList import TermFreqList

class Token(object):
    def __init__(self, name, tf):
        self.name = name
        self.tf = TermFreqList(tf)

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return self.toString()

    def toString(self):
        res = ""
        return ("(%s, df:%d) -> [%s]" % (self.name, self.tf.len(), self.tf.toString()))

    def appendTF(self, tfNew):
        x = self.tf.appendTF(tfNew)
        return x
