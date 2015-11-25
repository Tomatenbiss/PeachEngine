class TermFreqList:

    def __init__(self, docTitle, value):
        self.tf = {}
        self.add(docTitle, value)

    def __str__(self):
        return self.toString()

    def toString(self):
        res = ""
        cnt = 0
        for i in self.tf.keys():
            res = ("%s(%s, %d)" % (res, i, self.tf[i]))
            cnt += 1
            if cnt < len(self.tf):
                res+= ", "
        return res

    def len(self):
        return len(self.tf)

    def at(self, token):
        return self.tf[token]

    def add(self, docTitle, value):
        if docTitle in self.tf.keys():
            x = self.tf[docTitle]
            self.tf[docTitle] = x + value
        else:
            self.tf[docTitle] = value

    def addTF(self, tf):
        self.tf.update(tf.tf)


    def getFreq(self, docTitle):
        if docTitle in self.tf.keys():
            return self.tf[docTitle]
        else:
            return -1

    def getDocFreq(self):
        return len(self.tf.keys())

    def getKeys(self):
        return self.tf.keys()
