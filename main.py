from PeachCrawler.Downloader import Downloader
from PeachCrawler.Frontier import Frontier
from PeachRanker.RankGraph import Page_Rank
import re
import collections
import math
from bs4 import BeautifulSoup
from Token import Token
from TermFreq import TermFreq
from TermFreqList import TermFreqList
from TokenList import TokenList
from textblob import TextBlob


#NOT NEEDED ANYMORE DUE TO RESTRUCTURING
#Stemming wird erstmal nicht implementiert aufgrund der Spezifizität
# def soupToString(soup):
#     text = ""
#     for i in soup.body.strings:
#         text += i;
#     return text

#Normalizes a text
def normalize(text):
    text = text.replace("\n", " ")
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("'", "")
    text = text.lower()
    text = text.strip()
    tokens = re.split('[\s]+', text)
    return tokens

#Returns a normalized string
def normalizedString(text):
    return ' '.join(getStringWithoutStopWords(normalize(text)))

#Get stopwords from file
f = open('stop_words.txt', 'r')
data = f.read()
stopWords = normalize(data)

#Removes stopwords from a string
def getStringWithoutStopWords(oldString):
    ret = [x for x in oldString if x not in stopWords]
    return ret

#NOT NEEDED ANYMORE DUE TO RESTRUCTURING
# #update dict with new tokens
# def updateTokenList(dic, title, tokenList):
#     for token in tokenList:
#         if token not in dic:
#             dic[token] = 1, [title]
#         else:
#             (x, xs) = dic[token]
#             x+=1
#             xs.append(title)
#             dic[token] = x, xs
#     return dic

#NOT NEEDED ANYMORE DUE TO RESTRUCTURING
# def createDocTuples(dic, title, tokenList):
#     for el in tokenList:
#         if el in dic:
#             title, x = dic[el]
#             x += 1
#             dic[el] = (title, x)
#         else:
#             dic[el] = (title, 1)
#     return dic

#NOT NEEDED ANYMORE DUE TO RESTRUCTURING
# def combineDocTupleLists(docTuples, docTuples2):
#     for t in docTuples2:
#         if t in docTuples:
#             x = docTuples[t]
#             docTuples[t] = [x, docTuples2[t]]
#         else:
#             docTuples[t] = [docTuples2[t]]
#     return docTuples

#To-Do: Put in wrapperclass
#Returns the "Index" datastructe
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

#Initiate Frontier with seed an print results
seed = [
    "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html",
    "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html",
    "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html",
    ]

frontier = Frontier(seed)
frontier.peaching()
print(frontier.pageStructure())

#Initiate Ranker and print results
rank = Page_Rank(frontier.pageStructureDic())
rank.initial_rank()
rank.do_it()


#Gets all documents provided by the Crawler
def getAllDocs():
    my_page_downloader = Downloader()
    my_list_of_destinations = frontier.pageLinks()
    soup = {}
    for i in range(8):
        soup[i] = BeautifulSoup(my_page_downloader.download(my_list_of_destinations[i]))
    return soup

#Turns a normalized Text into a collections.OrderedDict
def normTextToOrderedDict(normText):
    dic = collections.OrderedDict()
    l = [[x,normText.count(x)] for x in normText]
    for i in l:
        x,y = i
        dic[x] = y
    return dic

#Calculates tf-weight of a Token related to a specified document
def tf_weight(token, docTitle):
    frequence = token.tf.getFreq(docTitle)
    if frequence > 0:
        tf_weight = 1 + math.log10(frequence)
        return 1 + math.log10(frequence)
    else:
        return 0

#Calculates idf-weight of an object of class Token
def idf_weight(token):
    dft = token.tf.getDocFreq()
    return math.log10(float(8 / dft))

#Print all Documents
docs = getAllDocs()
for i in range(8):
    print("-" * 80)
    print(docs[i].title.text)
    print("-" * 80)
    print(docs[i].body.text)

#To-Do: Wrap a class "Index" around it
#Create and Print index-datastructure
TL = TokenList()
print("\n" * 4)
for i in range(8):
    docTitle = docs[i].title.text
    normText = getStringWithoutStopWords(normalize(docs[i].text))
    d = normTextToOrderedDict(normText)
    for j in d:
        TL.add(Token(j, docTitle, d[j]))
TL.getSortedTokenList()
print(TL)

#Calculates tf-idf weight of a token in a document
def tf_idf_weight(token, docTitle):
    return tf_weight(token, docTitle) * idf_weight(token)

#To-Do: Later to be put into function
#Print documentlengths
print("-" * 80)
print("Doclengths:\n")
page_lengths = collections.OrderedDict()
for token in TL.tokens:
    for page_id in token.tf.getKeys():
        if page_id not in page_lengths:
            page_lengths[page_id] = 0

        tf_idf_w = tf_idf_weight(token, page_id)
        page_lengths[page_id] += tf_idf_w ** 2#aufaddierung der quadrierten tfidfWeights

for page_id, page in page_lengths.items():
    page_lengths[page_id] = math.sqrt(page_lengths[page_id])
for i in page_lengths:
    print(i, ": ", page_lengths[i])
print("-" * 80)




#To-Do: Later to be put into function
#print cosineScore
print("CosineScore\n")
query_tokens = ["tokens", "index", "classification"]#oder eben eine Liste für die Doppelsuche

for qtoken in query_tokens:
    wtq = idf_weight(TL.getTokenByName(qtoken))
    docList = TL.getTokenByName(qtoken).tf.getKeys()
    print("\n\"%s\"" % qtoken)
    for i in docList:
        print(i, tf_idf_weight(TL.getTokenByName(qtoken), i) * wtq / page_lengths[i] / wtq)

query_length = 0
page_scores = {}
query_length = 0
print("\n\"tokens\", \"classification\"")
for term in ["tokens", "classification"]:
    wtq = idf_weight(TL.getTokenByName(term))
    docList = TL.getTokenByName(term).tf.getKeys()
    query_length += wtq ** 2
    for i in docList:
        tf_idf_w = tf_idf_weight(TL.getTokenByName(term), i)
        if i not in page_scores:
            page_scores[i] = 0
        page_scores[i] += tf_idf_w * wtq
query_length = math.sqrt(query_length)
for i in page_scores.keys():
    print("#", i, page_scores[i] / page_lengths[i] / query_length)




#To-Do: Later to be put into function
#Print cosinescore combined with Pagerank
print("-" * 80)
print("Cosine combined with Pagerank")

ranks = rank.rank_graph_new
for qtoken in query_tokens:
    wtq = idf_weight(TL.getTokenByName(qtoken))
    docList = TL.getTokenByName(qtoken).tf.getKeys()
    print("\n\"%s\"" % qtoken)
    for i in docList:
        print(i, tf_idf_weight(TL.getTokenByName(qtoken), i) * wtq / page_lengths[i] / wtq * ranks[i])

query_length = 0
page_scores = {}
query_length = 0
print("\n\"tokens\", \"classification\"")
for term in ["tokens", "classification"]:
    wtq = idf_weight(TL.getTokenByName(term))
    docList = TL.getTokenByName(term).tf.getKeys()
    query_length += wtq ** 2
    for i in docList:
        tf_idf_w = tf_idf_weight(TL.getTokenByName(term), i)
        if i not in page_scores:
            page_scores[i] = 0
        page_scores[i] += tf_idf_w * wtq
query_length = math.sqrt(query_length)
for i in page_scores.keys():
    print("#", i, page_scores[i] / page_lengths[i] / query_length * ranks[i])
