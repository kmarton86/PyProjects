from bs4 import BeautifulSoup as bs
import requests
import os
import datetime
#pip install google

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
"""
query : query string that we want to search for.
tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
lang : lang stands for language.
num : Number of results we want.
start : First result to retrieve.
stop : Last result to retrieve. Use None to keep searching forever.
pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
"""

query = "j r r tolkien"

talalatok = []  
for j in search(query, tld="hu", lang="hun" ,num=100, stop=100, pause=2): 
    print(j) 
    talalatok.append(j)

today = datetime.date.today()
currentDirectory = os.getcwd()
fileName = '\googleSearch_' + str(today)
fullPath = str(currentDirectory) + fileName + ".txt"
with open(fullPath, 'w', encoding="utf-8") as filehandle:
    for listitem in talalatok:          
        try:
            filehandle.write('%s\n' % listitem)
        except Exception as e:
            filehandle.write('%s\n' % 'there was a failure to capture data: '+ str(e))