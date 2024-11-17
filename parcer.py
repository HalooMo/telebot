
from bs4 import BeautifulSoup
import requests 
import string

we_have = ""


def get_html_text(elem):
    global we_have
    if elem:
        for child in elem.children:
            if hasattr(child, "text"):
                we_have = we_have + child.text
            else:
                pass
    

r = requests.get(r"https://ru.wikipedia.org/wiki/Противовирусные_препараты")

 
soup = BeautifulSoup(r.text, 'lxml')
ref1 = soup.find_all("div", {"class": "reflist reflist-columns references-column-width"})
for y in ref1:
    y.clear()
ref3 = soup.find_all("div", {"class": "mw-heading mw-heading2"})
for j in ref3:
    j.clear()
ref2 = soup.find_all("sup")
for i in ref2:
    i.clear()
ref4 = soup.find_all("div", {"class":"vector-body ve-init-mw-desktopArticleTarget-targetContainer"})
for g in ref4:
    g.clear()
ref5 = soup.find_all("div", {"class":"catlink"})
for g in ref5:
    g.clear()
ref6 = soup.find_all("div", {"class":"mw-footer-container"})
for g in ref6:
    g.clear()
    
    
get_html_text(soup)
we_have.replace("[edit]", " ")
print(we_have)


bad_word = string.punctuation
bad_word.replace(".","")
bad_word.replace(",","")



for i in bad_word:
    we_have = we_have.replace(i,"")

we_have = we_have.split("\n")
data = ""
for i in we_have:
    if len(i) > 380:
        data = data + "\n" + i
    else:
        pass

print(data)
