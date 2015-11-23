#Crawler.
#It will init. a frontier object and starts the method peaching.
#This will do all the work to aquire the goal from "Uebung 1.1 Crawler"

from Frontier import Frontier
from Downloader import Downloader

seed = [
    "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html",
    "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html",
    "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html",
    ]

frontier = Frontier(seed)
frontier.peaching()
print(frontier.pageStructure())
#print(frontier.pageLinks())
#print(frontier.pageStructureDic())
