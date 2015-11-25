import itertools
from Downloader import Downloader
from Frontier import Frontier
import re
import collections
import math
from bs4 import BeautifulSoup
from Token import Token
from TermFreq import TermFreq
from TermFreqList import TermFreqList
from TokenList import TokenList
from RankGraph import Page_Rank

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

def normalizedString(text):
    return ' '.join(getStringWithoutStopWords(normalize(text)))

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
            title, x = dic[el]
            x += 1
            dic[el] = (title, x)
        else:
            dic[el] = (title, 1)
    return dic

def combineDocTupleLists(docTuples, docTuples2):
    for t in docTuples2:
        if t in docTuples:
            x = docTuples[t]
            docTuples[t] = [x, docTuples2[t]]
        else:
            docTuples[t] = [docTuples2[t]]
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

def getAllDocs():
    seed = [
        "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html",
        "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html",
        "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html",
        ]

    frontier = Frontier(seed)
    frontier.peaching()
    print (frontier.pageStructure())

    my_page_downloader = Downloader()
    my_list_of_destinations = frontier.pageLinks()
    soup = {}

    for i in range(8):
        soup[i] = BeautifulSoup(my_page_downloader.download(my_list_of_destinations[i]))
    return soup

def normTextToOrderedDict(normText):
    dic = collections.OrderedDict()
    l = [[x,normText.count(x)] for x in normText]
    for i in l:
        x,y = i
        dic[x] = y
    return dic

def tf_weight(frequence):
    if frequence > 0:
        tf_weight = 1 + math.log10(frequence)
        return 1 + math.log10(frequence)

def dft_weight(token):
    dft = TL.getDocFreq(token)
    return math.log10(float(8 / dft))

#Hier gehts weiter
TL = TokenList()

##finalText = getStringWithoutStopWords(normalize(docs[2].text))
#finalText.sort()
#doctitle = "d01"
#print(finalText)
#print(finalText.count(finalText[0]))



#for i in dic:
    #TL.add(Token(i, TermFreq(title, dic[i])))
#TL.add(Token("all", TermFreq("d02", 1)))


docs = getAllDocs()

for i in range(8):
    print("-" * 80)
    print(docs[i].title.text)
    print("-" * 80)
    print(docs[i].body.text)

rank = Page_Rank()
rank.initial_rank()
rank.do_it()
print("\n" * 4)
for i in range(8):
    docTitle = docs[i].title.text
    normText = getStringWithoutStopWords(normalize(docs[i].text))
    d = normTextToOrderedDict(normText)
    for j in d:
        TL.add(Token(j, TermFreq(docTitle, d[j])))


TL.getSortedTokenList()


print(TL)

#return self.tf_weight(term, page_id) * self.idf_weight(term)
#TermFreq = 1 + math.log10(frequence)
#ft = DocFreq



#print(TL.getDocFreq("document"))
#tokensTermFreq = [1, 2, 1, 2, 0, 0, 0, 4]
#indexTermFreq = [0, 0, 0, 1, 2, 0, 0, 4]
#classificationTermFreq = [0, 0, 0, 0, 0, 1, 1, 4]



#print("tfweight:", tf_weight)
#frequence = itf.at(0).termFreq#termFreq im Doc, wenn Term vorhanden -> 1+math.log10(f)
#for i in tokensTermFreq:
    #if i > 0:
        #print(tf_weight(i) * dft_weight("tokens"))


#TL.getTermFreq("tokens", "d01")






#print("###TFIDF:", self.tf_weight(term, page_id) * self.idf_weight(term))
#print(tf_weight * dft_weight)


#print(i.tf.len())









































#Ausgabe mit FakeDaten
#tf = [TermFreq("d01", 1), TermFreq("d01", 1),TermFreq("d02", 3)]
#TOList = []
#tfl = TermFreqList(tf)
#for el in tokenList:
    #TOList.append(Token(el, 1, tfl))


#def tf(word, blob):
       #return blob.words.count(word) / len(blob.words)
#
#def n_containing(word, bloblist):
    #return 1 + sum(1 for blob in bloblist if word in blob)
#
#def idf(word, bloblist):
   #return math.log(float(1+len(bloblist)) / float(n_containing(word,bloblist)))
#
#def tfidf(word, blob, bloblist):
   #return tf(word, blob) * idf(word, bloblist)


#bloblist = []
#for i in range(8):
    #bloblist.append(TextBlob(docs[i].text))


#print(tf("tokens", bloblist[0]))
#print(idf("tokens", bloblist))
#print(tfidf("tokens", bloblist[0], bloblist))
#print tf_score, idf_score, tfidf_score
