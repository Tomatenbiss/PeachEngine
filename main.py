from PeachRank.RankGraph import Page_Rank
from PeachCrawler.Frontier import Frontier

seed = [
    "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html",
    "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html",
    "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html",
    ]

frontier = Frontier(seed)
frontier.peaching()
print(frontier.pageStructure())

rank = Page_Rank()
rank.initial_rank()
rank.do_it()
