#Crawler.
#It will init. a frontier object and starts the method peaching.
#This will do all the work to aquire the goal from "Übung 1.1 Crawler"


#   from Frontier import Frontier
#
#   seed = [
#           'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html',
#           'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html',
#           'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html',
#          ]
#   frontier = Frontier(seed)
#   frontier.peaching()

from Downloader import Downloader

download = Downloader('www.google.de')
print(download)
