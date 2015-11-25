from Token import Token

class TokenList:
    def __init__(self):
        self.tokens = []

    def __str__(self):
        ret = ""
        for i in self.tokens:
            ret+=("%s\n" % i.toString())
        return ret


    def add(self, name):
        if self.contains(name):
            for token in self.tokens:
                if token.name == name.name:
                    token = token.appendTF(name.tf)
        else:
            self.tokens.append(name)

    def contains(self, name):
        for token in self.tokens:
            if token.name == name.name:
                return True
        return False

    def getSortedTokenList(self):
        self.tokens.sort()

    def getTokenByName(self, name):
        for i in self.tokens:
            if i.name == name:
                return i

    def getDocFreq(self, token):
        tmp = self.getTokenByName(token)
        return tmp.tf.len()

    def getTermFreq(self, token, docTitle):
        tmp = self.getTokenByName(token)
        itf = tmp.tf
        #for i in itf.len():
        print("tfl:", itf.at(3))



    #def add(self, token):
        #if not self.contains(token):

        #else:
            #print(self.tokens[token])
            #print("ja")
