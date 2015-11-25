class TermFreqList:
    def __init__(self, tf):
        self.tf = [tf]

    def __str__(self):
        return self.toString()

    def toString(self):
        res = ""
        cnt = 0
        for i in self.tf:
            res+=i.toString()
            cnt += 1
            if cnt < len(self.tf):
                res+= ", "
        return res

    def len(self):
        return len(self.tf)

    def at(self, index):
        return self.tf[index]

    def getLen(self):
        return len(self.tf)

    def appendTF(self, tfNew):
        self.tf.append(tfNew)
