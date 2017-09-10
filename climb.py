from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import sql

pages=set()

def getlink(newpage, recursionLevel):
    global pages
    if recursionLevel > 4:
        return;
    frompage_id = sql.insertPageIfNotExists(newpage)
    url = urlopen("https://en.wikipedia.org"+newpage)
    html = BeautifulSoup(url,"lxml")
    print(html.title.get_text())
    links = html.findAll("a",href=re.compile("^/wiki/((?!:).)*$"))
    for link in links:
        href = link.attrs['href']
        if href not in pages:
            topage_id=sql.insertPageIfNotExists(href)
            sql.insertLink(frompage_id, topage_id)
            pages.add(href)
            print(href)
            getlink(href,recursionLevel+1)


getlink("/wiki/Main_Page",0)