import re
from bs4 import BeautifulSoup

#Stemming wird erstmal nicht implementiert aufgrund der Spezifizität
def soupToString(soup):
    text = ""
    for i in soup.body.strings:
        text += i;
    return text

def normalize(text):
    text = text.replace("\n", " ")
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("'", "")
    text = text.lower()
    text = text.strip()
    tokens = re.split('[\s]+', text)
    return tokens

#Get stopwords from file
f = open('stop_words.txt', 'r')
data = f.read()
stopWords = normalize(data)

def getStringWithoutStopWords(oldString):
    ret = [x for x in oldString if x not in stopWords]
    return ret

#update dict with new tokens
def updateTokenList(dic, title, tokenList):
    for token in tokenList:
        if token not in dic:
            dic[token] = 1, [title]
        else:
            (x, xs) = dic[token]
            x+=1
            xs.append(title)
            dic[token] = x, xs
    return dic

def createDocTuples(dic, title, tokenList):
    for el in tokenList:
        if el in dic:
            (title, x) = dic[el]
            x += 1
            dic[el] = title, x
        else:
            dic[el] = title, 1
    return dic

def combineDocTupleLists(docTuples, docTuples2):
    for t in docTuples2:
        if t in docTuples:
            x = docTuples[t]
            docTuples[t] = x, docTuples2[t]
        else:
            docTuples[t] = docTuples2[t]
    return docTuples


#Make soups for each page
soup1 = BeautifulSoup(open("d01.html"))
soup2 = BeautifulSoup(open("d02.html"))
soup3 = BeautifulSoup(open("d03.html"))
soup4 = BeautifulSoup(open("d04.html"))
soup5 = BeautifulSoup(open("d05.html"))
soup6 = BeautifulSoup(open("d06.html"))
soup7 = BeautifulSoup(open("d07.html"))
soup8 = BeautifulSoup(open("d08.html"))

def getIndexDataStructure():
    dic = {}
    tokenList = getStringWithoutStopWords(normalize(soupToString(soup1)))
    tokenList.sort();
    docTuples = createDocTuples(dic, "d01", tokenList)

    dic2 = {}
    tokenList = getStringWithoutStopWords(normalize(soupToString(soup2)))
    tokenList.sort();
    docTuples2 = createDocTuples(dic2, "d02", tokenList)
    return combineDocTupleLists(docTuples, docTuples2)

#Try around -> getDocFreqTerm
ds = getIndexDataStructure()
term ="character"
x = 0

l = ds[term]
print(l)
