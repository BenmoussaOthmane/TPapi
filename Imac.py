import requests 
from bs4 import BeautifulSoup
# import pandas  
import json




acceder = requests.get('https://www.ouedkniss.com/imac_informatique-r?')

code = acceder.content

prised = BeautifulSoup(code , 'html.parser')

all = prised.find_all("div", {"class":"annonce"})
# nbr = len(all)
# div = all[0].find("span" , {"itemprop":"price"})

liste = []

for tou in all:
    d = {}
    try:
        d["nome"] = tou.find("h2" , {"itemprop":"name"}).text.replace(" \n" , "").replace("\r" , "").replace("/" , "")
        
    except: 
        pass

    try:
        d["cati"] = tou.find("span", {"class" : "annonce_get_description"}).text.replace("\n" , "").replace("\r", "").replace(" " ,"").replace("/" , "")
        
    except:
        pass

    try:
        d["price"] = tou.find("span", {"itemprop":"price"}).text.replace("\n" , "").replace("\r" ,"").replace(" ","").replace("/", "")
        
    except:
        pass
    
    try:
        d["wilaya"] = tou.find("span" , {"class" :"titre_wilaya"}).text.replace("\n", "").replace("/" , "").replace("\r" , "")
        
    except:
        pass
     
    liste.append(d)
    print(d)
with open('jsd.json', 'w') as f:
    f.write(json.dumps(liste,indent=4, sort_keys=True))



