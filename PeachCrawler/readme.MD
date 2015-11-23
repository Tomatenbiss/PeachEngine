# How to use
***
Attention: The Crawler.py is just a wrapper for the crawler consisting of Frontier.py, Parser.py, Downloader.py
***
## Get the page structure:

If you want the page-structure you can use the following methods: 

### First
`# Make sure the frontier is allready done: `  
`# frontier = Frontier(seed)`  
`# frontier.peaching()`  
`string_classen = frontier.pageStructure() `  

The output is the following:   
d01:d02,d03,d04  
d02:d03,d04,d01,d05  
d03:d04,d01,d02,d05  
d04:d01,d02,d03,d05  
d05:d04  
d06:d07  
d07:d06  
d08:  

### Second 
`# Make sure the frontier is allready done: `  
`# frontier = Frontier(seed)`  
`# frontier.peaching()`  
`my_dic_structure = frontier.pageStructureDic()`
`# print ( my_dic_structure )`

The output is the following:  
{'d07': ['d06'],  
'd06': ['d07'],  
'd05': ['d04'],  
'd04': ['d01', 'd02', 'd03', 'd05'],  
'd03': ['d04', 'd01', 'd02', 'd05'],  
'd02': ['d03', 'd04', 'd01', 'd05'],  
'd01': ['d02', 'd03', 'd04'],  
'd08': ['']}
  
Note: Dictionaries in Python are not sorted


***
## Get a list of all destinations

If you want a full list of all destinations use: 

`# Make sure the frontier is allready done: `  
`# frontier = Frontier(seed)`  
`# frontier.peaching()`  
`list_of_pages_to_lookup = frontier.pageLinks()`  


This will give you the following list: 

['http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html',  
'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d02.html',  
'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d03.html',  
'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d04.html',  
'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d05.html',
'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html',  
'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d07.html',  
'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html']  


***
## Download the source of a specific destination:

If you want to download the source of a destination use: 

`# Make sure the frontier is allready done: `  
` my_page_downloader = Downloader() `  
` my_list_of_destinations = frontier.pageLinks() `  
` my_downloaded_page = my_page_downloader.download(my_list_of_destinations[0]) `  
` # print source`  

This will give you the following output: 

<a href="http://imgur.com/ZuZddEt"><img src="http://i.imgur.com/ZuZddEt.png" title="source: imgur.com" /></a>


